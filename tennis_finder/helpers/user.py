"""Is authenticated helper."""
from flask_login import current_user


def is_authenticated() -> bool:
    """
    Check if user is authenticated.

    :return: true if user is authenticated else false
    """
    return current_user.is_authenticated
