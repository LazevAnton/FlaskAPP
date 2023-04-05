from app.auth.forms import EditProfileForm
from app.main import bp
from flask import render_template
from app.models import User
from app import db


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='MainPage')


@bp.route('/about')
def about():
    return render_template('about.html', title='About')


@bp.route('/profile')
def profile():
    user_query = db.session.query(User)
    users = user_query.all()
    print(users)
    return render_template('profile.html', users=users, title='Profile')


@bp.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    return render_template('edit_profile.html', form=form)
