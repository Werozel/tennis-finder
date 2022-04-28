from flask_login import current_user


def is_authenticated():
    return current_user.is_authenticated
