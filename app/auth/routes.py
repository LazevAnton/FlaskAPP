from app.auth import bp
from flask import render_template, redirect
from .forms import LoginForm, RegisterForm


@bp.route('/')
def index():
    return render_template('auth/index.html', title='Auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('auth/login.html', title='Login', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('auth/register.html', title='Register', form=form)

