from random import randint

from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffPlayer import MijnlieffPlayer
from games.mijnlieff.MijnlieffState import MijnlieffState
from games.mijnlieff.MijnlieffPieceType import MijnlieffPieceType
from games.state import State


class RandomMijnlieffPlayer(MijnlieffPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MijnlieffState):
        possible_actions = state.get_possible_actions()

        if len(possible_actions) == 0:
            return None

        return possible_actions[randint(0, len(possible_actions) - 1)]

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
