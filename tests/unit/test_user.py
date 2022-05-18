from werkzeug.datastructures import FileStorage

from tests.helpers.random_user import get_random_user


def test_user():
    default_name = "static/profile_pics/default.jpg"
    with open(default_name, "rb") as f:
        pic = FileStorage(stream=f, filename=default_name)
        user = get_random_user()
        user.set_user_picture(pic)

    assert user.image_file_path
    path = user.image_file_path

    user.delete_user_picture()
    assert user.image_file_path != path

    user.wins = 10
    user.losses = 0
    assert user.get_win_rate() == "100%"

    user.losses = 5
    assert user.get_win_rate() == "50%"

    user.wins = 0
    assert user.get_win_rate() == "0.0%"
