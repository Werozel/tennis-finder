import faker
from wtforms import ValidationError

from modules.users.forms.register import RegistrationForm
from modules.users.models.user import User


class PasswordContainer:
    def __init__(self, data_container):
        self.password = data_container


class DataContainer:
    def __init__(self, data):
        self.data = data


def test_register_form_validations(_db, db_session):
    fake = faker.Faker()

    fake_phone = "+79169999999"  # Faker`s phones not always counted as real
    RegistrationForm.validate_phone(None, DataContainer(fake_phone))
    user = User(phone=fake_phone, full_name=fake.name(), login=fake.user_name(), password=fake.password(), skill=2)
    db_session.add(user)
    db_session.commit()

    try:
        RegistrationForm.validate_phone(None, DataContainer(fake_phone))
    except ValidationError:
        pass
    else:
        assert False

    RegistrationForm.validate_email(None, DataContainer(fake.email()))
    password = fake.password()
    RegistrationForm.validate_confirm_password(
        PasswordContainer(DataContainer(password)), DataContainer(password)
    )
    try:
        RegistrationForm.validate_confirm_password(
            PasswordContainer(DataContainer(password)), DataContainer("Wrong")
        )
    except ValidationError:
        pass
    else:
        assert False


