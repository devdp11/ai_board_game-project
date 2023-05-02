
from games.mijnlieff.MijnlieffPieceType import MijnlieffPieceType

class MijnlieffPiece:
    __piece_type: MijnlieffPieceType

    def __init__(self, piece_type: MijnlieffPieceType, player: int):
        self.piece_type = piece_type
        self.player = player

    def get_type(self):
        return self.__piece_type
