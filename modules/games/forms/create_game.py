import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeLocalField
from wtforms.validators import DataRequired, Length, Email, ValidationError


class CreateGameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=100)])
    game_date = DateTimeLocalField('Game date', validators=[DataRequired()], format="%d-%m-%Y %H:%M",
                                   default=lambda: datetime.datetime.now() + datetime.timedelta(days=1))

    submit = SubmitField('Create')
