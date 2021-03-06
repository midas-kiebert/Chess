from coordinates import Coord

WHITE = 1
BLACK = 0


class Piece:
    def __init__(self, color: bool, pos: Coord):
        self.color = color
        self.moved = False
        self.en_passant = False
        self.pos = pos

    # def __repr__(self):
    #     if self.color == BLACK:
    #         return f'\033[1;31m{self.char}'
    #     return f'\033[1;39m{self.char}'

    def __bool__(self):
        return not isinstance(self, Empty)


class Pawn(Piece):
    char = 'P'

    def __init__(self, color: bool, pos: Coord):
        super().__init__(color, pos)
        self.id = 'pw' if color else 'pb'

    def potential_moves(self):
        moves = []
        if self.color == BLACK:
            moves += [Coord(i, 1) for i in range(-1, 2)]
            if not self.moved:
                moves += [Coord(0, 2)]
        else:
            moves += [Coord(i, -1) for i in range(-1, 2)]
            if not self.moved:
                moves += [Coord(0, -2)]
        return moves


class King(Piece):
    char = 'K'

    def __init__(self, color: bool, pos: Coord):
        super().__init__(color, pos)
        self.id = 'kw' if color else 'kb'

    def potential_moves(self):
        if self.moved:
            return [Coord(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        return [Coord(i, j) for i in range(-1, 2) for j in range(-1, 2)] + [Coord(-2, 0), Coord(2, 0)]


class Queen(Piece):
    char = 'Q'

    def __init__(self, color: bool, pos: Coord):
        super().__init__(color, pos)
        self.id = 'qw' if color else 'qb'

    def potential_moves(self):
        return [Coord(0, i) for i in range(-7, 8)] +\
               [Coord(i, 0) for i in range(-7, 8)] +\
               [Coord(i, i) for i in range(-7, 8)] +\
               [Coord(i, -i) for i in range(-7, 8)]

class Rook(Piece):
    char = 'R'

    def __init__(self, color: bool, pos: Coord):
        super().__init__(color, pos)
        self.id = 'rw' if color else 'rb'

    def potential_moves(self):
        return [Coord(0, i) for i in range(-7, 8)] +\
               [Coord(i, 0) for i in range(-7, 8)]


class Bishop(Piece):
    char = 'B'

    def __init__(self, color: bool, pos: Coord):
        super().__init__(color, pos)
        self.id = 'bw' if color else 'bb'

    def potential_moves(self):
        return [Coord(i, i) for i in range(-7, 8)] +\
               [Coord(i, -i) for i in range(-7, 8)]


class Knight(Piece):
    char = 'N'

    def __init__(self, color: bool, pos: Coord):
        super().__init__(color, pos)
        self.id = 'nw' if color else 'nb'

    def potential_moves(self):
        return [Coord(i, j) for i in (-1, 1) for j in (-2, 2)] +\
               [Coord(i, j) for i in (-2, 2) for j in (-1, 1)]


class Empty(Piece):
    char = ' '

    def __init__(self):
        super().__init__(0, Coord(-1, -1))
