from modules.core.app import app

from modules.users.models.user import User


@app.route("/users")
def get_users():
    return []

