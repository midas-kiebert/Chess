WHITE = 1
BLACK = 0


class Piece:
    def __init__(self, color: bool):
        self.color = color

    def __repr__(self):
        if self.color == BLACK:
            return f'\033[1;31m{self.char}'
        return f'\033[1;39m{self.char}'

    def __bool__(self):
        return not isinstance(self, Empty)


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


class Empty(Piece):
    char = ' '

    def __init__(self):
        super().__init__(0)
