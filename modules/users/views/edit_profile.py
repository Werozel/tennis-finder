from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from modules.core.app import app
from modules.core.db import db
from modules.users.forms.edit_profile import EditProfileForm
from modules.users.models.skill import valid_skills
from modules.users.models.user import User


@app.route("/profile/edit", methods=['get'])
@login_required
def render_edit_profile():
    user: User = current_user
    form = EditProfileForm(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        skill=user.skill,
        current_user_email=user.email,
        current_user_phone=user.phone
    )
    form.skill.data = user.skill
    return render_template("edit_profile.html", user=user, form=form, skills=valid_skills)


@app.route("/profile/edit", methods=['post'])
@login_required
def submit_edit_profile():
    user: User = current_user
    form = EditProfileForm(
        current_user_email=user.email,
        current_user_phone=user.phone
    )
    if not form.validate_on_submit():
        form.skill.data = user.skill
        return render_template("edit_profile.html", user=user, form=form, skills=valid_skills)

    user.full_name = form.full_name.data
    user.email = form.email.data
    user.phone = form.phone.data
    user.skill = form.skill.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('render_profile'))
