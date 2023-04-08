from app.auth import bp
from flask import render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user
from .. import db
from ..models import User, Profile
from ..service import UserService

user_service = UserService()


@bp.route('/')
def index():
    return render_template('auth/index.html', title='Auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username/password", category="error")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('user.profile', username=user.username))
    return render_template('auth/login.html', title='Login', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if user or email:
            flash('Username or email already exist', category='error')
            return redirect(url_for('auth.register'))
        user_service.create(username=form.username.data, email=form.email.data, password=form.password.data)
        # user = User(username=form.username.data, email=form.email.data)
        # user.set_password(form.password.data)
        # db.session.add(user)
        # db.session.commit()
        # profile = Profile(
        #     user_id=user.id
        # )
        # db.session.add(profile)
        # db.session.commit()
        flash("Successfully registered!", category="success")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=register, form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
