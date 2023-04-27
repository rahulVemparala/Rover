"""
Register and login forms and various fields

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(), Length(2, 20)])
    email = StringField('email', validators=[
        DataRequired(), Email()])
    password = StringField('password', validators=[
        DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[
        DataRequired(), Email()])
    password = StringField('password', validators=[
        DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
