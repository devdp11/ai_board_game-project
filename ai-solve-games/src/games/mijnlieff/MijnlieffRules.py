from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffState import MijnlieffState
 
class MijnlieffRules():

    def __display_Rules(self, row, col, choice):
        print({
            0: 1['+'],
            0: 2['x'],
            0: 3['o'],
            0: 4['0'],
            1: 1['+'],
            1: 2['x'],
            1: 3['o'],
            1: 4['0'],
            MijnlieffState.EMPTY_CELL: ' '
        }[self.__grid[row][col]], end="")
        
        choice = int(input("Escolha uma peça para jogar:"))


    def __display_Piece(self, row, col, player):
        self.__num_rows = row
        self.__num_cols = col
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                if player == 1:
                    self.__num_rows
                    
                    
        print([])
        pass

    def __validate_play(self, player):

        pass