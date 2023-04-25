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
                return MijnlieffAction(int(input(f"Player {state.get_acting_player()}, Escolha uma Coluna:")), int(input(f"Player {state.get_acting_player()}, Escolha uma Linha:")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: MijnlieffState):
        # ignore
        pass

    def event_end_game(self, final_state: MijnlieffState):
        # ignore
        pass
