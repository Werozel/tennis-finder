"""This module contains create game form."""
from gettext import gettext

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeLocalField
from wtforms.validators import DataRequired, Length, InputRequired


class CreateGameForm(FlaskForm):
    """This is the create game form."""

    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=100)])
    game_date = DateTimeLocalField('Game date', validators=[InputRequired()], format="%Y-%m-%dT%H:%M")

    submit = SubmitField('Create')
