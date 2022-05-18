from dataclasses import dataclass

from modules.games.models.games import Game
from modules.users.models.user import User


@dataclass
class SearchGame:
    """Model to sort games in search screen"""

    game: Game
    opponent_skill: float
    opponent_win_rate: float

    def get_sorting_score(self, opponent_skill: float, opponent_win_rate: float) -> float:
        """
        Get sorting score for the game.

        :param opponent_skill: float skill value of the opponent
        :param opponent_win_rate: float win rate value of the opponent
        :return: float sorting score
        """

        return 10 * abs(opponent_skill - self.opponent_skill) + \
            abs(opponent_win_rate - self.opponent_win_rate)

    @staticmethod
    def from_game(game: Game) -> 'SearchGame':
        """
        Create SearchGame model from Game model

        :param game: Game obj to build SearchGame upon
        :return: SearchGame
        """
        opponent: User = game.players[0]
        return SearchGame(
            game=game,
            opponent_skill=opponent.skill,
            opponent_win_rate=opponent.get_win_rate()
        )
