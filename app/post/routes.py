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
        flash('Sorry, but you have already liked this post', category='warning')
    post_like = Like(user=current_user, post=post)
    db.session.add(post_like)
    db.session.commit()
    flash('Thank you, you have liked this post')
    return redirect(request.referrer)


@bp.route('/<int:post_id>/dislike', methods=['GET', 'POST'])
@login_required
def dislike(post_id):
    post = Post.query.get_or_404(post_id)
    if Like.query.filter_by(user=current_user, post=post).count() > 0:
        flash('Sorry, but you have already disliked this post', category='warning')
    post_dislike = Dislike(user=current_user, post=post)
    db.session.add(post_dislike)
    db.session.commit()
    flash('Thank you, you have disliked this post')
    return redirect(request.referrer)


@bp.route('/<int:post_id>/delete', methods=['GET', 'POST'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('You have deleted you post', category='success')
    return redirect(url_for('user.blog'))
