from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError


class ContactForm(FlaskForm):
    name = TextField('Name of Student', [validators.Required('Please enter your name.')])

    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')

    email = TextField('Email', [validators.Required('Please enter your email address.'),
                                validators.Email('Please enter a valid email address.')])

    Age = IntegerField('Age', [validators.Required('Please enter your age.')])
    language = SelectField('Languages',
                           choices=[('py', 'Python'), ('js', 'javascript'), ('css', 'Css'), ('html', 'Html')])
    submit = SubmitField('Send')


