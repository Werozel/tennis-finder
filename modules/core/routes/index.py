from flask import url_for, redirect

from modules.core.app_config import AppConfig

app = AppConfig.app


@app.route("/")
def render_index():
    return redirect(url_for("render_profile"))
