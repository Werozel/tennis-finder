import re

import phonenumbers as phonenumbers
from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from modules.users.models.skill import valid_skills
from modules.users.models.user import User


skill_choices = list(
    map(
        lambda x: (x.value, x.title),
        valid_skills
    )
)


class RegistrationForm(FlaskForm):
    full_name = StringField('Full name', validators=[DataRequired(), Length(min=3, max=100)])
    login = StringField('Login', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[Length(max=12)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired()])
    skill = SelectField('NTRP Rating', choices=skill_choices)

    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_phone(_, phone):
        p = phonenumbers.parse(phone.data)
        if not phonenumbers.is_valid_number(p):
            raise ValidationError(gettext('Invalid phone number'))

        user = User.query.filter_by(phone=phone.data)
        if user:
            raise ValidationError(gettext('This phone number is taken'))

    @staticmethod
    def validate_login(_, login):
        if not re.match("^[A-Za-z0-9_-]*$", login.data):
            raise ValidationError(gettext('Login can only contain letters, numbers, underscores and dashes'))
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError(gettext('This username is already taken'))

    @staticmethod
    def validate_email(_, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(gettext('Account with this email already exists'))

    @staticmethod
    def validate_confirm_password(form, confirm_password):
        if not form.password.data == confirm_password.data:
            raise ValidationError(gettext("Passwords doesn't match!"))
