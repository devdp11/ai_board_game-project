import math 
from random import choice
from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffPlayer import MijnlieffPlayer
from games.mijnlieff.MijnlieffState import MijnlieffState
from games.mijnlieff.MijnlieffPieceType import MijnlieffPieceType

from games.state import State


class GreedyMijnlieffPlayer(MijnlieffPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MijnlieffState):

        grid = state.get_grid()

        
        max_count = 0

        #check each line
        for row in range(0, state.get_num_rows()):
            seq = 0
            for col in range(0, state.get_num_cols()):
                if grid[row][col] == self.get_current_pos():
                    seq += 1
                else:
                    if seq > max_count:
                        max_count = seq
                    seq = 0
            if seq > max_count:
                max_count = seq
        # check each column
        for col in range(0, state.get_num_cols()):
            seq = 0
            for row in range(0, state.get_num_rows()):
                if grid[row][col] == self.get_current_pos():
                    seq += 1
                else:
                    if seq > max_count:
                        max_count = seq
                    seq = 0
            if seq > max_count:
                max_count = seq
        # check each upward diagonl
        for row in range(2, state.get_num_rows()):
            for col in range(0, state.get_num_cols() -2):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row -1][col + 1] == self.get_current_pos() else 0)
                
                seq2 = (1 if grid[row -1][col +1] == self.get_current_pos() else 0) +\
                       (1 if grid[row -2][col +2] == self.get_current_pos() else 0)
                
                if seq1 > max_count:
                    max_count = seq1

                if seq2 > max_count:
                    max_count = seq2
        # check each downward diagonal
        for row in range(0, state.get_num_rows() -2):
            for col in range(0, state.get_num_cols() -2):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row +1][col + 1] == self.get_current_pos() else 0)
                
                seq2 = (1 if grid[row +1][col +1] == self.get_current_pos() else 0) +\
                       (1 if grid[row +2][col +2] == self.get_current_pos() else 0)
                
                if seq1 > max_count:
                    max_count = seq1
                if seq2 > max_count:
                    max_count = seq2
        return max_count
    def get_action(self, state: MijnlieffState):
        selected_actions = None
        value = -match.inf
        for action in state.get_possible_actions():
            pre_valoe = value
            value = max(value, self.__heuristic(state.sim_play(action)))
            if value == pre_valoe:
                selected_actions.append(action)
            if value > pre_valoe:
                selected_actions = [action]
        if selected_actions is None:
            raise Exception("there is no valid action")
        return state.get_closest_to_center(selected_actions)
    def event_action(self, pos: int, action, new_state: State):
        
        #ignore
        pass
    def event_end_game(self, final_state: State):
        
        #ignore
        pass
