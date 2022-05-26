from werkzeug.datastructures import FileStorage

from tennis_finder.modules.core.app_config import AppConfig
from tennis_finder.tests.helpers.random_user import get_random_user


def test_user():
    default_name = "tennis_finder/static/profile_pics/default.jpg"
    with open(default_name, "rb") as f:
        pic = FileStorage(stream=f, filename=default_name)
        user = get_random_user()
        user.set_user_picture(pic)

    assert user.image_file_path
    path = user.image_file_path

    user.delete_user_picture()
    assert user.image_file_path != path

    with AppConfig.app.app_context():
        user.wins = 10
        user.losses = 0
        assert user.get_win_rate() == 1

        user.losses = 10
        assert user.get_win_rate() == 0.5

        user.wins = 0
        assert user.get_win_rate() == 0
