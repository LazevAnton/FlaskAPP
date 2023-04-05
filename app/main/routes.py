from app.auth.forms import EditProfileForm
from app.main import bp
from flask import render_template
from app.models import User
from app import db


@bp.route('/')
@bp.route('/index')
def index():
    user_query = db.session.query(User)
    users = user_query.all()
    print(users)
    return render_template('index.html', user=users)

    # flask_users = [
    #     {
    #         'username': 'test10',
    #         'email': 'test10@gmail.com',
    #         'password': 'passwdtest1'
    #     },
    #     {
    #         'username': 'test11',
    #         'email': 'test11@gmail.com',
    #         'password': 'passwdtest2'
    #     },
    #     {
    #         'username': 'test12',
    #         'email': 'test12@gmail.com',
    #         'password': 'passwdtest3'
    #     },
    # ]
    # for data in flask_users:
    #     user_data = db.session.query(User).filter(
    #         User.username == data.get('username'),
    #         User.email == data.get('email')
    #     )
    #     if user_data:
    #         continue
    #     user_data = User(
    #         username=data.get('username'),
    #         email=data.get('email'),
    #         password=data.get('password')
    #     )
    #     db.session.add(user_data)
    # db.session.commit()
    # return render_template('index.html', title='FlaskAPP')


@bp.route('/about')
def about():
    return render_template('about.html', title='About')


@bp.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')


@bp.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    return render_template('edit_profile.html', form=form)
