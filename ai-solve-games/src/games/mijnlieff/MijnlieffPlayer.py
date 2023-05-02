
from abc import ABC

from games.mijnlieff.MijnlieffResult import MijnlieffResult
from games.player import Player


class MijnlieffPlayer(Player, ABC):

    def __init__(self, name):
        super().__init__(name)
        self.__stats = {None: 0, "win": 0, "loss": 0, "draw": 0}


        """
        stats is a dictionary that will store the number of times each result occurred
        """
        self.__stats = {}
        for c4res in MijnlieffResult:
            self.__stats[c4res] = 0

        """
        here we are storing the number of games
        """
        self.__num_games = 0

    def print_stats(self):
        num_wins = self.__stats[MijnlieffResult.WIN]
        if num_wins > 0:
            print(
                f"Player {self.get_name()}: {num_wins}/{self.__num_games} wins ({num_wins * 100.0 / self.__num_games} win "
                f"rate)")
        num_draws = self.__stats[MijnlieffResult.DRAW]
        if num_draws > 0:
            print("Draw!")

    def event_new_game(self):
        self.__num_games += 1

    def event_result(self, pos: int, result: MijnlieffResult):
        if pos == self.get_current_pos() and result is not None:
            self.__stats[result] += 1