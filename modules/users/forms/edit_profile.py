import phonenumbers
from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from modules.users.forms.register import skill_choices
from modules.users.models.user import User


class EditProfileForm(FlaskForm):
    full_name = StringField('Full name', validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[Length(max=12)])
    skill = SelectField('NTRP Rating', choices=skill_choices)

    submit = SubmitField('Sign Up')

    def __init__(self, current_user_email, current_user_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user_email = current_user_email
        self.current_user_phone = current_user_phone

    def validate_phone(self, phone):
        p = phonenumbers.parse(phone.data)
        if not phonenumbers.is_valid_number(p):
            raise ValidationError(gettext('Invalid phone number'))
        if self.current_user_phone == phone.data:
            return

        user = User.query.filter_by(phone=phone.data)
        if user:
            raise ValidationError(gettext('This phone number is taken'))

    def validate_email(self, email):
        if self.current_user_email == email.data:
            return
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(gettext('Account with this email already exists'))
