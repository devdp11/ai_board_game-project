from random import randint

from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffPlayer import MijnlieffPlayer
from games.mijnlieff.MijnlieffState import MijnlieffState
from games.state import State


class RandomMijnlieffPlayer(MijnlieffPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MijnlieffState):
        return MijnlieffAction(randint(0, state.get_num_cols()), randint(0, state.get_num_rows()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
