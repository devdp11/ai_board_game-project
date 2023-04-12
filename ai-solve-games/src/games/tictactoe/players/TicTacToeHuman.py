from games.tictactoe.TicTacToeAction import TicTacToeAction
from games.tictactoe.TicTacToePlayer import TicTacToePlayer
from games.tictactoe.TicTacToeState import TicTacToeState


class HumanTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return TicTacToeAction(int(input(f"Player {state.get_acting_player()}, Choose a Column: ")), int(input(f"Player {state.get_acting_player()}, Choose a Row: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: TicTacToeState):
        # ignore
        pass

    def event_end_game(self, final_state: TicTacToeState):
        # ignore
        pass
