"""
Register and login forms and various fields

"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from rover.database import User
from flask_login import current_user


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

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError(
                "Username already taken, please choose another one ")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(
                "Email Address already taken, please choose another one ")


class LoginForm(FlaskForm):
    email = StringField('email', validators=[
        DataRequired(), Email()])
    password = StringField('password', validators=[
        DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(), Length(2, 20)])
    email = StringField('email', validators=[
        DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError(
                    "Username already taken, please choose another one ")

    def validate_email(self, email):
        if email.data != current_user.email:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError(
                    "Email Address already taken, please choose another one ")
