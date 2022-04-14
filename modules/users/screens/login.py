from flask import render_template, redirect, flash

from modules.core.app import app
from modules.users.forms.LoginForm import LoginForm
from modules.users.models.user import User


@app.route("/users/login", methods=['GET'])
def render_login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/users/login", methods=['POST'])
def submit_login():

    form = LoginForm()
    username = form.username.data
    password = form.password.data # TODO hash
    user = User.query.filter_by(username=username, password=password).first()
    if user:

        # TODO complete
        return redirect('render_profile')
    else:
        # TODO translate and complete
        flash("Incorrect login!", "danger")
        return render_template("login.html", form=form)
