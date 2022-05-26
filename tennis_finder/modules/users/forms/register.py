"""This module contains registration form."""
import re

import phonenumbers as phonenumbers
from flask_babel import gettext
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileSize
from phonenumbers import NumberParseException
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, ValidationError, Optional

from tennis_finder.modules.users.models.skill import valid_skills
from tennis_finder.modules.users.models.user import User


skill_choices = list(
    map(
        lambda x: (x.value, x.title),
        valid_skills
    )
)


class RegistrationForm(FlaskForm):
    """This is the registration form."""

    full_name = StringField('Full name', validators=[DataRequired(), Length(min=3, max=100)])
    picture = FileField('Profile image', validators=[FileAllowed(['jpg', 'png', 'jpeg']), FileSize(3_145_728)])
    login = StringField('Login', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[Optional(strip_whitespace=True), Email()])
    phone = StringField('Phone', validators=[Optional(strip_whitespace=True), Length(max=12)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired()])
    skill = SelectField('NTRP Rating', choices=skill_choices)

    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_phone(_, phone):
        """Validate phone and check that it's not taken."""
        if not phone.data:
            return
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError
        except (NumberParseException, ValueError):
            raise ValidationError(gettext('Invalid phone number'))

        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError(gettext('This phone number is taken'))

    @staticmethod
    def validate_login(_, login):
        """Validate user login and check that it's not taken."""
        if not re.match("^[A-Za-z0-9_-]*$", login.data):
            raise ValidationError(gettext('Login can only contain letters, numbers, underscores and dashes'))
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError(gettext('This username is already taken'))

    @staticmethod
    def validate_email(_, email):
        """Validate if email is already taken."""
        if not email.data:
            return
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(gettext('Account with this email already exists'))

    @staticmethod
    def validate_confirm_password(form, confirm_password):
        """Validate passwords match."""
        if not form.password.data == confirm_password.data:
            raise ValidationError(gettext("Passwords doesn't match!"))
