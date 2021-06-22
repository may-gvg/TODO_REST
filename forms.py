from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField ('description', validators=[DataRequired()])
    done = BooleanField('done' )

