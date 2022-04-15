from helpers.args import get_cookie
from modules.core.app import babel


@babel.localeselector
def get_locale():
    return get_cookie('language', 'ru')


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone
