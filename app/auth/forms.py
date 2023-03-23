from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember = BooleanField('Remember')
    submite = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submite = SubmitField('Login')