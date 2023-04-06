from flask_login import login_required
from .forms import EditProfileForm
from app.user import bp
from flask import render_template, flash
from .. import db
from ..models import User


@bp.route('/profile')
@login_required
def profile():
    user_query = db.session.query(User)
    users = user_query.all()
    print(users)
    return render_template('profile.html', users=users, title='Profile')


@bp.route('/edit_profile/<string:username>', methods=['GET', 'POST'])
def edit_profile(username):
    user = db.session.query(User).filter(User.username == username).first_or_404()
    form = EditProfileForm()
    if form.validate_on_submit():
        user.profile.first_name = form.first_name.data
        user.profile.last_name = form.last_name.data
        user.profile.linkedIn_url == form.linkedin_url.data
        user.profile.facebook_url == form.facebook_url.data
        user.profile.bio == form.bio.data
        db.session.commit()
        flash('Your changes has been set', category='success')
    return render_template('edit_profile.html', form=form)
