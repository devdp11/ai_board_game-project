from typing import List, Tuple, Optional
from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffResult import MijnlieffResult
from games.mijnlieff.MijnlieffPieceType import MijnlieffPieceType
from games.state import State


class MijnlieffState(State):
    EMPTY_CELL = -1

    def __init__(self, rows: int = 4, cols: int = 4):
        super().__init__()

        if rows != 4 or cols != 4:
            raise Exception("The Mijnlieff board must be 4x4")

        self.__num_rows = rows
        self.__num_cols = cols

        self.__last_move = None

        self.__grid = [[(-1, None) for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        self.__turns_count = 1

        self.__acting_player = 0

        self.__has_winner = False
                
        self.__size = 4

    def __count_sequences(self, player):
        count = 0
        # check for 3 across
        for row in range(0, self.__size - 1):
            for col in range(0, self.__size - 2):
                if self.__grid[row][col][0] == player and \
                        self.__grid[row][col + 1][0]  == player and \
                        self.__grid[row][col + 2][0]  == player:
                    count += 1

        # check for 3 up and down
        for row in range(0, self.__size - 2):
            for col in range(0, self.__size - 1):
                if self.__grid[row][col][0]  == player and \
                        self.__grid[row + 1][col][0]  == player and \
                        self.__grid[row + 2][col][0]  == player:
                    count += 1

        # check upward diagonal
        for row in range(2, self.__size):
            for col in range(0, self.__size - 2):
                if self.__grid[row][col][0]  == player and \
                        self.__grid[row - 1][col + 1][0]  == player and \
                        self.__grid[row - 2][col + 2][0]  == player:
                    count += 1

        # check downward diagonal
        for row in range(0, self.__size - 2):
            for col in range(0, self.__size - 2):
                if self.__grid[row][col][0]  == player and \
                        self.__grid[row + 1][col + 1][0]  == player and \
                        self.__grid[row + 2][col + 2][0]  == player:
                    count += 1

        return count

    def get_grid(self):
        return self.__grid

    

    def get_num_players(self):
        return 2

    def validate_action(self, action: MijnlieffAction) -> bool:
        if action is None:
            return False

        row = action.get_row()
        col = action.get_col()

        if col < 0 or col >= self.__num_cols:
            return False
        if row < 0 or row >= self.__num_rows:
            return False
        if self.__grid[row][col][0] != -1:
            return False

        return self.is_valid_move(action)

    def update(self, action: MijnlieffAction):
        row = action.get_row()
        col = action.get_col()
        piece = action.get_type()

        player = self.get_acting_player()
        
        self.__grid[row][col] = (player, piece)

        if self.__is_full() or len(self.get_possible_actions()) == 0:
            self.__has_winner = self.__check_winner()

        self.__last_move = action

        self.__acting_player = 1 if self.__acting_player == 0 else 0
        self.__turns_count += 1

    def __check_winner(self):
        p0_seqs = self.__count_sequences(0)
        p1_seqs = self.__count_sequences(1)

        
        if p0_seqs > p1_seqs:
            return 0
        elif p1_seqs > p0_seqs:
            return 1
        else:
            return -1

    def is_valid_move(self, action: MijnlieffAction):
        last_action = self.get_last_move()
        
        if last_action is None:
            return True  # No restriction for the first move of each player

        current_col = last_action.get_col()
        current_row = last_action.get_row()
        target_col = action.get_col()
        target_row = action.get_row()
        row_diff = abs(target_row - current_row)
        col_diff = abs(target_col - current_col)

        piece_type = last_action.get_type()
        """print(f"piece type: {piece_type}")"""
        if piece_type == MijnlieffPieceType.S:
            return col_diff == 0 or row_diff == 0
        elif piece_type == MijnlieffPieceType.D:
            return col_diff == row_diff
        elif piece_type == MijnlieffPieceType.H:
            return (col_diff >= 2 and row_diff >= 0) or (col_diff >= 0 and row_diff >= 2) or (col_diff > 1 and row_diff > 0) or (col_diff > 0 and row_diff > 1) or (col_diff >= 2 and row_diff >= 2)
        elif piece_type == MijnlieffPieceType.L:
            return (col_diff == 1 and row_diff == 0) or (col_diff == 0 and row_diff == 1) or (col_diff == 1 and row_diff == 1)
        
        return False

    def get_last_move(self) -> Optional[MijnlieffAction]:
        return self.__last_move
    
    def display_cell(self, row, col):
            cell = self.__grid[row][col]
            if cell[0] == -1:
                print("  ", end="")
            else:
                player, piece = cell
                # Convert the integer piece to a MijnlieffPieceType
                piece = MijnlieffPieceType(piece)
                print(f"{piece.name}{player + 1}", end="")

    def __display_numbers(self):
        for col in range(self.__num_cols):
            print("   ", end=" ")
            print(col, end=" ")
        print("  ")

    def __display_separator(self):
        for col in range(self.__num_cols):
            print("------", end="")
        print("")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(self.__num_rows):
            print("", row, "", end="")
            print('|', "", "", end="")
            for col in range(self.__num_cols):
                self.display_cell(row, col)
                print('|', "", "", end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__is_full() or  len(self.get_possible_actions()) == 0

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = MijnlieffState(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[MijnlieffResult]:
        if self.__has_winner:
            if self.__has_winner == -1:
                return MijnlieffResult.DRAW

            return MijnlieffResult.LOOSE if pos == self.__acting_player else MijnlieffResult.WIN
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
            grid: list[list[int]] = []
            for i in range(self.get_num_rows()):
                for j in range(self.get_num_cols()):
                    grid.append([i, j])

            possible_actions = []
            for pos in grid:
                for piece in MijnlieffPieceType:
                    action = MijnlieffAction(pos[0], pos[1], piece)
                    if self.validate_action(action):
                        possible_actions.append(action)

            return possible_actions

    def sim_play(self, action):
        new_state = self.clone()
        new_state.update(action)
        return new_state