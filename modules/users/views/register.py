from flask import render_template

from modules.core.app import app
from modules.users.forms.register import RegistrationForm


@app.route("/users/register", methods=['GET'])
def render_register():
    form = RegistrationForm()
    return render_template("register.html", form=form)



