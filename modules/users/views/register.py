"""This module contains /users/register routes."""
from flask import render_template, redirect, url_for, make_response
from flask_login import login_user

from helpers import crypto
from helpers.args import get_arg_or_none
from modules.core.app_config import AppConfig
from modules.users.forms.register import RegistrationForm
from modules.users.models.skill import valid_skills
from modules.users.models.user import User


app = AppConfig.app
db = AppConfig.db


@app.route("/users/register", methods=['GET'])
def render_register():
    """Render GET /users/register request screen."""
    form = RegistrationForm()
    return render_template("register.html", form=form, skills=valid_skills)


@app.route("/users/register", methods=['POST'])
def submit_register():
    """Create user with provided credentials."""
    form = RegistrationForm()
    if not form.validate_on_submit():
        return render_template("register.html", form=form, skills=valid_skills)

    login = form.login.data
    user = User(
        full_name=form.full_name.data,
        login=login,
        password=crypto.hash_password(form.password.data, login),
        email=form.email.data,
        phone=form.phone.data,
        skill=form.skill.data
    )
    picture = form.picture.data
    if picture:
        user.set_user_picture(picture)

    db.session.add(user)
    db.session.commit()

    login_user(user, remember=True, force=True)
    next_page = get_arg_or_none('next')
    resp = make_response(redirect(next_page) if next_page else redirect(url_for('render_profile')))
    resp.set_cookie('language', 'ru')
    return resp
