from flask import render_template
from flask_login import current_user, login_required

from modules.core.app import app
from modules.games.models.games import GameStatus
from modules.users.models.user import User


@app.route("/my_games", methods=['get'])
@login_required
def render_my_games():
    user: User = current_user
    all_games = user.games
    pending_games = list(
        filter(
            lambda x: x.status == GameStatus.PENDING,
            all_games
        )
    )
    progress_games = list(
        filter(
            lambda x: x.status == GameStatus.IN_PROGRESS,
            all_games
        )
    )
    completed_games = list(
        filter(
            lambda x: x.status == GameStatus.COMPLETED,
            all_games
        )
    )

    return render_template(
        "my_games.html",
        pending_games=pending_games,
        progress_games=progress_games,
        completed_games=completed_games
    )
