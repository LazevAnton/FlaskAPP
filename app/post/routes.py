from os import abort
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from app import db
from app.models import Post, Like, Dislike
from app.post import bp
from app.post.forms import PostForm


@bp.route('/create', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post(title=form.post_title.data, content=form.post_content.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Excellent, your post has been created', category='success')
        else:
            title = form.post_title.data
            if not title or len(title) < 2:
                flash('Sorry, title must be at least two characters long', category='error')
        return redirect(url_for('user.blog', user=current_user))
    return render_template('user/blog.html', form=form, title='Create post')


@bp.route('/<int:post_id>/like', methods=['GET', 'POST'])
@login_required
def like(post_id):
    post = Post.query.get_or_404(post_id)
    if Like.query.filter_by(user=current_user, post=post).count() > 0:
        flash('Sorry, but you already like this post😎', category='warning')
    else:
        post_like = Like(user=current_user, post=post)
        db.session.add(post_like)
        db.session.commit()
        flash('Thanks, i knew this post get likes🤪', category='success')
    return redirect(request.referrer)


@bp.route('/<int:post_id>/dislike', methods=['GET', 'POST'])
def dislike(post_id):
    post = Post.query.get_or_404(post_id)
    if Dislike.query.filter_by(user=current_user, post=post).count() > 0:
        flash('Sorry, but you already dislike this post😪', category='warning')
    else:
        post_dislike = Dislike(user=current_user, post=post)
        db.session.add(post_dislike)
        db.session.commit()
        flash('What?are you seriously?my post is magnificent', category='success')

    return redirect(request.referrer)


@bp.route('/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    post_delete = Post.query.get_or_404(post_id)
    if post_delete.author != current_user:
        abort(403)
    else:
        db.session.delete(post_delete)
        db.session.commit()
        flash('Your post has been deleted', category='success')
    return redirect(url_for('user.blog'))
