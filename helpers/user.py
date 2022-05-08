"""Is authenticated helper."""
from flask_login import current_user


def is_authenticated():
    """Check if user is authenticated."""
    return current_user.is_authenticated
