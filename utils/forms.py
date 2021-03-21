from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from ..models.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=5, max=30)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=5, max=30)])
    user_email = EmailField('Email', validators=[
                            DataRequired(), Length(min=5, max=30), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    accept = BooleanField('Accept conditions')
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.objects(name=username.data).first()
        if user:
            raise ValidationError(
                message='Account with given username already exists. Try a different one.')

    def validate_user_email(self, user_email):
        user = User.objects(email=user_email.data).first()
        if user:
            raise ValidationError(
                message='Account with given email already exists. Try a different one.')


class CreateIssue(FlaskForm):
    title = StringField('Title', validators=[
                        DataRequired(), Length(min=5, max=30)])
    description = TextAreaField(
        'Description', validators=[DataRequired(), Length(min=5, max=300)])
    submit = SubmitField('Create')
