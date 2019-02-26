from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class RegistrationForm(FlaskForm):
    '''Form for adding new user'''
    username = StringField('Username:', 
                            validators=[InputRequired()])

    password = StringField('Password:', 
                            validators=[InputRequired()])