from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    validators,
    SubmitField,
    TextAreaField,

)
from wtforms.validators import Length


class EditProfileForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    linkedin_url = StringField('Linkedin')
    facebook_url = StringField('Facebook')
    bio = TextAreaField('About me', validators=[Length(min=0, max=200)])
    submit = SubmitField('Submit')
