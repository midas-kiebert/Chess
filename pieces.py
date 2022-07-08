


class Piece:
    WHITE = 1
    BLACK = 0

    def __init__(self, color: bool):
        self.color = color

    def __repr__(self):
        if self.color == Piece.BLACK:
            return f'\033[1;31m{self.char}\033[1;31m'
        return f'\033[1;34m{self.char}\033[1;34m'


class Pawn(Piece):
    char = 'P'

    def __init__(self, color: bool):
        super().__init__(color)


class King(Piece):
    char = 'K'

    def __init__(self, color: bool):
        super().__init__(color)


class Queen(Piece):
    char = 'Q'

    def __init__(self, color: bool):
        super().__init__(color)


class Rook(Piece):
    char = 'R'

    def __init__(self, color: bool):
        super().__init__(color)


class Bishop(Piece):
    char = 'B'

    def __init__(self, color: bool):
        super().__init__(color)


class Knight(Piece):
    char = 'N'

    def __init__(self, color: bool):
        super().__init__(color)