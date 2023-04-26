from games.mijnlieff.MijnlieffPieceType import MijnlieffPieceType

class MijnlieffAction:

    __col: int
    __row: int
    __type: str

    def __init__(self, col: int, row: int, type: MijnlieffPieceType):
        self.__col = col
        self.__row = row
        self.__type = type

    def get_col(self):
        return self.__col
    
    def get_row(self):
        return self.__row
    
    def get_type(self) -> MijnlieffPieceType:
        return self.__type