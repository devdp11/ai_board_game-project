from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffPlayer import MijnlieffPlayer
from games.mijnlieff.MijnlieffState import MijnlieffState


class HumanMijnlieffPlayer(MijnlieffPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MijnlieffState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                piece = int(input(f"Player {state.get_acting_player()}, Escolha uma Peça (1-4): "))
                if piece not in range(1, 5):
                    print("Invalid piece. Please choose a piece between 1 and 4.")
                    continue

                col = int(input(f"Player {state.get_acting_player()}, Escolha uma Coluna: "))
                row = int(input(f"Player {state.get_acting_player()}, Escolha uma Linha: "))
                action = MijnlieffAction(row, col, piece)

                if state.validate_action(action):
                    return action
                else:
                    print("Invalid move. Please try again.")
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: MijnlieffState):
        # ignore
        pass

    def event_end_game(self, final_state: MijnlieffState):
        # ignore
        pass