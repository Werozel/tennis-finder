from dataclasses import dataclass

from modules.games.models.games import Game
from modules.users.models.user import User


@dataclass
class SearchGame:

    game: Game
    opponent_skill: float
    opponent_win_rate: float

    def get_sorting_score(self, opponent_skill: float, opponent_win_rate: float) -> float:
        return 10 * abs(opponent_skill - self.opponent_skill) + \
               abs(opponent_win_rate - self.opponent_win_rate)

    @staticmethod
    def from_game(game: Game) -> 'SearchGame':
        opponent: User = game.players[0]
        return SearchGame(
            game=game,
            opponent_skill=opponent.skill,
            opponent_win_rate=opponent.get_win_rate()
        )
