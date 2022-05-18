import faker

from helpers.crypto import hash_password


def test_hash_password():
    fake = faker.Faker()
    login, password = fake.user_name(), fake.password()

    hash_1 = hash_password(password, login)

    assert hash_1  # Hash not empty
    assert hash_1 == hash_password(password, login)  # It`s not random one
    assert hash_1 != hash_password("different_password", login)  # They are different for different passwords
    assert hash_1 != hash_password(password, "different_login")  # They are unique for each user
