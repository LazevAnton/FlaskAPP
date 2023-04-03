from app.auth import bp
from flask import render_template, redirect, url_for,flash
from .forms import LoginForm, RegisterForm
from flask_login import current_user


@bp.route('/')
def index():
    return render_template('auth/index.html', title='Auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    # if form.validate_on_submit():
    #     flash
    #     return redirect(url_for('auth.index'))
    # return render_template('auth/login.html', title='Login', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('auth.index'))
    return render_template('auth/register.html', title='Register', form=form)
