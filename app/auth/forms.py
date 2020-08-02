from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    preferred_time = RadioField('Preferred time', choices=[(
        'Morning', 'morning'), ('Noon', 'noon'), ('Evening', 'evening')], validators=[DataRequired()])
    # categories
    politics = BooleanField('Politics')
    sports = BooleanField('Sports')
    finance = BooleanField('Finance')
    lifestyle = BooleanField('Lifestyle')
    submit = SubmitField('Register')
