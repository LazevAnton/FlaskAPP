from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    validators,
    PasswordField,
    BooleanField,
    SubmitField,
    EmailField
)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired(message='Username is required')])
    password = PasswordField('Password', validators=[validators.DataRequired(message='Password is required'),
                                                     validators.Length(min=8,
                                                                       message='Min 6 length of password is required')])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    email = EmailField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submit = SubmitField('Register')
