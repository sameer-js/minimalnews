from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, RadioField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('PasswordField', validators=[
                             DataRequired(), Length(min=6, message='Password must be atleast 6 characters long.')])
    preferred_time = RadioField('Preferred time', choices=[(
        'Morning', 'morning'), ('Noon', 'noon'), ('Evening', 'evening')])
    submit = SubmitField('Sign Up')
