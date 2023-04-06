from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    validators,
    PasswordField,
    BooleanField,
    SubmitField,
    EmailField
)
from wtforms.validators import Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired(message='Username is required')])
    password = PasswordField('Password', validators=[validators.DataRequired(message='Password is required'),
                                                     validators.Length(min=8,
                                                                       message='Min 6 length of password is required')])

    remember = BooleanField('Remember')
    submit = SubmitField('Login')


class RegisterForm(LoginForm):
    email = EmailField('Email', validators=[validators.DataRequired(message="Email is required"), validators.Email()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            validators.DataRequired(message="Confirm password is required"),
            validators.EqualTo("password", message="Passwords should match")
        ]
    )
    submit = SubmitField('Register')
