from app.main import bp
from flask import render_template
from app.models import User,Profile
from app import db


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='MainPage')


@bp.route('/about')
def about():
    return render_template('about.html', title='About')

