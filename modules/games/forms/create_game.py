import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeLocalField
from wtforms.validators import DataRequired, Length, InputRequired


class CreateGameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=100)])
    game_date = DateTimeLocalField('Game date', validators=[InputRequired()])

    submit = SubmitField('Create')
