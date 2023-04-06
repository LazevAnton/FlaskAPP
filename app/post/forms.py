from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
    post_content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Create Post')
