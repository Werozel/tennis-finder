from flask import render_template
from flask_login import login_required

from modules.core.app import app


@app.route("/profile", methods=['get'])
@login_required
def render_profile():

    return render_template("profile.html")
