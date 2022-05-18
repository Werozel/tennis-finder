from tests.helpers.random_user import get_random_user
from modules.games.models.games import Game, GameStatus


def test_game(db_session):
    game = Game(name="Test game")
    db_session.add(game)
    db_session.commit()

    assert game.id
    assert game.status == GameStatus.PENDING

    user = get_random_user()
    game.add_player(user)
    db_session.add(user)
    db_session.add(game)
    db_session.commit()
    assert game.status == GameStatus.PENDING

    try:
        game.add_player(user)
    except ValueError:
        pass
    else:
        assert True

    game.add_player(get_random_user())
    assert game.status == GameStatus.IN_PROGRESS
