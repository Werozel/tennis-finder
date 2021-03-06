"""This module contains /users/login routes."""
from gettext import gettext

from flask import render_template, redirect, flash, url_for, make_response
from flask_login import login_user

from tennis_finder.helpers import crypto
from tennis_finder.helpers.args import get_arg_or_none
from tennis_finder.modules.core.app_config import AppConfig
from tennis_finder.modules.users.forms.login import LoginForm
from tennis_finder.modules.users.models.user import User


app = AppConfig.app


@app.route("/users/login", methods=['GET'])
def render_login():
    """Render login page."""
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/users/login", methods=['POST'])
def submit_login():
    """Try to log in user with provided credentials."""
    form = LoginForm()
    login = form.login.data
    password = crypto.hash_password(form.password.data, login)
    user = User.query.filter_by(login=login, password=password).first()
    if user:
        login_user(user, remember=form.remember.data, force=True)
        next_page = get_arg_or_none('next')
        resp = make_response(redirect(next_page) if next_page else redirect(url_for('render_profile')))
        resp.set_cookie('language', 'ru')
        return resp
    else:
        flash(gettext("Incorrect login!"), "danger")
        return render_template("login.html", form=form)
