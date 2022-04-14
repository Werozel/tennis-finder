from modules.core.app import app


@app.route("/users/register", methods=['GET'])
def render_register():
    return ""
