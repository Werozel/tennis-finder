from flask import request, make_response, redirect
from flask_login import current_user

from helpers.args import get_arg_or_none
from modules.core.app import app
from modules.core.db import db


@app.route("/change_language")
def change_language_route():
    new_language = get_arg_or_none('language')
    if new_language not in ['en', 'ru']:
        curr_language = request.cookies.get('language')
        if curr_language == 'en':
            new_language = 'ru'
        else:
            new_language = 'en'
    resp = make_response(redirect(request.referrer))
    resp.set_cookie('language', new_language)
    return resp
