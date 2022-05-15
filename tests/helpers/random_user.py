import faker

from modules.users.models.user import User

fake = faker.Faker()


def get_random_user():
    user = User(
        phone=fake.numerify("+###########"),
        full_name=fake.name(),
        login=fake.user_name(),
        password=fake.password(),
        skill=2
    )
    return user
