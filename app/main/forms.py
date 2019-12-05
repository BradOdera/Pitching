from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    description = TextAreaField('Your Post', validators=[Required()])
    author = StringField('Your Name', validators=[Required()])
    submit = SubmitField('Submit')
