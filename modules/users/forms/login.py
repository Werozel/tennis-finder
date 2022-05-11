"""This module contains login form."""
from gettext import gettext

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """This is the login form."""

    login = StringField(gettext('Login'), validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField(gettext('Password'), validators=[DataRequired()])
    remember = BooleanField(gettext('Remember me'))
    submit = SubmitField(gettext('Login'))
