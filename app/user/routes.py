from flask_login import login_required, current_user
from .forms import ProfileForm
from app.user import bp
from flask import render_template, flash, redirect, url_for, request
from .. import db
from ..models import User, Post, Follow
from ..post.forms import PostForm


@bp.route('/blog')
@login_required
def blog():
    form = PostForm()
    posts = (
        db.session.query(Post)
        .filter(
            Post.author_id == current_user.id
        )
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template('user/blog.html', posts=posts, form=form)


@bp.route('/profile/<string:username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = db.session.query(User).filter(User.username == username).first_or_404()
    form = ProfileForm()
    if form.validate_on_submit():
        user.profile.first_name = form.first_name.data
        user.profile.last_name = form.last_name.data
        user.profile.linkedIn_url = form.linkedin_url.data
        user.profile.facebook_url = form.facebook_url.data
        user.profile.bio = form.bio.data
        db.session.commit()
        flash('Your profile has been saved', category='success')
        return redirect(url_for('user.profile', username=user.username))
    elif request.method == 'GET':
        form.first_name.data = user.profile.first_name
        form.last_name.data = user.profile.last_name
        form.linkedin_url.data = user.profile.linkedIn_url
        form.facebook_url.data = user.profile.facebook_url
        form.bio.data = user.profile.bio
    return render_template('user/profile.html', title='Profile', form=form, user=user)


@bp.route('/follow/<int:user_id>', methods=['POST'])
@login_required
def follow_user(user_id):
    user_to_follow = db.session.query(User).filter(User.username == user_id).first_or_404()
    if not user_to_follow:
        flash('User not found.', category='error')
        return redirect(url_for('user.profile', username=user_to_follow.username))

    if current_user.is_following(user_to_follow):
        flash('You are already following this user.', 'info')
        return redirect(url_for('user_profile', username=user_to_follow.username))

    follow = Follow(follow=current_user, followee=user_to_follow)
    db.session.add(follow)
    db.session.commit()

    flash(f'You are now following {user_to_follow.username}.', 'success')
    return redirect(url_for('user_profile', username=user_to_follow.username))