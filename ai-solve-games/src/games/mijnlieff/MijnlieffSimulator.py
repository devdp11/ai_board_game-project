from games.mijnlieff.MijnlieffPlayer import MijnlieffPlayer
from games.mijnlieff.MijnlieffState import MijnlieffState
from games.game_simulator import GameSimulator


class MijnlieffSimulator(GameSimulator):

    def __init__(self, player1: MijnlieffPlayer, player2: MijnlieffPlayer, num_rows: int = 5, num_cols: int = 5):
        super(MijnlieffSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the connect4 grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return MijnlieffState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: MijnlieffState):
        # ignored for this simulator
        pass

    def end_game(self, state: MijnlieffState):
        # ignored for this simulator
        pass
