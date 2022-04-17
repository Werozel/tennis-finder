from flask import render_template, redirect, url_for, make_response
from flask_login import login_user

from helpers.args import get_arg_or_none
from modules.core.app import app
from modules.core.db import db
from modules.users.forms.register import RegistrationForm
from modules.users.models.user import User


@app.route("/users/register", methods=['GET'])
def render_register():
    form = RegistrationForm()
    return render_template("register.html", form=form)


@app.route("/users/register", methods=['POST'])
def submit_register():
    form = RegistrationForm()
    if not form.validate_on_submit():
        return render_template("register.html", form=form)

    user = User(
        full_name=form.full_name.data,
        login=form.login.data,
        password=form.password.data,
        email=form.email.data,
        phone=form.phone.data,
        skill=form.skill.data
    )

    db.session.add(user)
    db.session.commit()

    login_user(user, remember=True, force=True)
    next_page = get_arg_or_none('next')
    # TODO: redirect to choose skill
    resp = make_response(redirect(next_page) if next_page else redirect(url_for('render_profile')))
    resp.set_cookie('language', 'ru')
    return resp
