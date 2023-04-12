from random import randint

from games.tictactoe.TicTacToeAction import TicTacToeAction
from games.tictactoe.TicTacToePlayer import TicTacToePlayer
from games.tictactoe.TicTacToeState import TicTacToeState
from games.state import State


class RandomTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState):
        return TicTacToeAction(randint(0, state.get_num_cols()), randint(0, state.get_num_rows()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
