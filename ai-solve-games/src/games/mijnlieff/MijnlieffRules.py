from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffState import MijnlieffState
 
class MijnlieffRules():

    def __display_Rules(self, row, col):
        print({
            0: 'Peça  Straights',
            1: 'Peça  Diagonals',
            3: 'Peça  Pushers',
            4: 'Peça  Pullers',
            MijnlieffState.EMPTY_CELL: ' '
        }[self.__grid[row][col]], end="")
        
        choice = int(input("Escolha uma peça para jogar:"))


    def __display_Piece(self, row, col):
        self.__num_rows = row
        self.__num_cols = col
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                if player == 1:
                    
        print([])
        pass

    def __validate_play(self, player):

        pass