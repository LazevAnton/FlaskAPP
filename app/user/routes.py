from flask_login import login_required
from .forms import ProfileForm
from app.user import bp
from flask import render_template, flash, redirect, url_for, request
from .. import db
from ..models import User


@bp.route('/index')
def index():
    return render_template('user/flaskapp.html', title='FlaskAPP')


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
