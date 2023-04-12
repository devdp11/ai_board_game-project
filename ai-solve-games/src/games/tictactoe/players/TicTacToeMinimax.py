import math

from games.tictactoe.TicTacToePlayer import TicTacToePlayer
from games.tictactoe.TicTacToeState import TicTacToeState
from games.tictactoe.TicTacToeResult import TicTacToeResult
from games.state import State


class MinimaxTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    '''
    This heuristic will simply count the maximum number of consecutive pieces that the player has
    It's not a great heuristic as it doesn't take into consideration a defensive approach
    '''

    def __heuristic(self, state: TicTacToeState):
        grid = state.get_grid()
        longest = 0

        # check each line
        for row in range(0, state.get_num_rows()):
            seq = 0
            for col in range(0, state.get_num_cols()):
                if grid[row][col] == self.get_current_pos():
                    seq += 1
                else:
                    if seq > longest:
                        longest = seq
                    seq = 0

            if seq > longest:
                longest = seq

        # check each column
        for col in range(0, state.get_num_cols()):
            seq = 0
            for row in range(0, state.get_num_rows()):
                if grid[row][col] == self.get_current_pos():
                    seq += 1
                else:
                    if seq > longest:
                        longest = seq
                    seq = 0

            if seq > longest:
                longest = seq

        # check each upward diagonal
        for row in range(3, state.get_num_rows()):
            for col in range(0, state.get_num_cols() - 3):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 1][col + 1] == self.get_current_pos() else 0)

                seq2 = (1 if grid[row - 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 2][col + 2] == self.get_current_pos() else 0)
                
                if seq1 > longest:
                    longest = seq1

                if seq2 > longest:
                    longest = seq2

        # check each downward diagonal
        for row in range(0, state.get_num_rows() - 3):
            for col in range(0, state.get_num_cols() - 3):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 1][col + 1] == self.get_current_pos() else 0)

                seq2 = (1 if grid[row + 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 2][col + 2] == self.get_current_pos() else 0)

                if seq1 > longest:
                    longest = seq1

                if seq2 > longest:
                    longest = seq2

        return longest

    """Implementation of minimax search (recursive, with alpha/beta pruning) :param state: the state for which the 
    search should be made :param depth: maximum depth of the search :param alpha: to optimize the search :param beta: 
    to optimize the search :param is_initial_node: if true, the function will return the action with max ev, 
    otherwise it return the max ev (ev = expected value) """

    def minimax(self, state: TicTacToeState, depth: int, alpha: int = -math.inf, beta: int = math.inf,
                is_initial_node: bool = True):
        # first we check if we are in a terminal node (victory, draw or loose)
        if state.is_finished():
            return {
                TicTacToeResult.WIN: 40,
                TicTacToeResult.LOOSE: -40,
                TicTacToeResult.DRAW: 0
            }[state.get_result(self.get_current_pos())]

        # if we reached the maximum depth, we will return the value of the heuristic
        if depth == 0:
            return self.__heuristic(state)

        # if we are the acting player
        if self.get_current_pos() == state.get_acting_player():
            # very small integer
            value = -math.inf
            selected_action = None

            for action in state.get_possible_actions():
                pre_value = value
                value = max(value, self.minimax(state.sim_play(action), depth - 1, alpha, beta, False))
                if value > pre_value:
                    selected_action = action
                if value > beta:
                    break
                alpha = max(alpha, value)

            return selected_action if is_initial_node else value

        # if it is the opponent's turn
        else:
            value = math.inf
            for action in state.get_possible_actions():
                value = min(value, self.minimax(state.sim_play(action), depth - 1, alpha, beta, False))
                if value < alpha:
                    break
                beta = min(beta, value)
            return value

    def get_action(self, state: TicTacToeState):
        return self.minimax(state, 5)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
