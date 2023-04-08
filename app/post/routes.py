from flask import request, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from app import db
from app.models import Post
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
        return redirect(url_for('user.blog'))
    return render_template('user/blog.html', title='Create Post', form=form)