from flask import render_template, abort
from flask_login import login_required, current_user

from modules.core.app import app
from modules.users.models.user import User


@app.route("/profile", methods=['get'])
@login_required
def render_profile():
    user = current_user
    return render_template("profile.html", user=user, my=True)


@app.route("/profile/<user_id>", methods=['get'])
@login_required
def render_user_profile(user_id: int):
    user = User.query.get(user_id)
    if not user:
        # TODO: default errors template
        abort(404)
    my = user.id == current_user.id
    return render_template("profile.html", user=user, my=my)


@app.route("/profile/edit", methods=['get'])
@login_required
def edit_profile():
    # TODO: complete and add check permission
    user = current_user
    return render_template("profile.html", user=user)