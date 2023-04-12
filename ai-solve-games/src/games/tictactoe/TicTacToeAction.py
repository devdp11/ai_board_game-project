class TicTacToeAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __col: int
    __row: int

    def __init__(self, col: int, row: int):
        self.__col = col
        self.__row = row

    def get_col(self):
        return self.__col
    
    def get_row(self):
        return self.__row