from numpy import isin
from coordinates import COORDINATES
from pieces import *

class Board:
    def __init__(self):
        self.board = [[Empty() for _ in range(8)] for _ in range(8)]
        self.black_rooks = [Rook(BLACK) for _ in range(2)]
        self.white_rooks = [Rook(WHITE) for _ in range(2)]
        self.black_bishops = [Bishop(BLACK) for _ in range(2)]
        self.white_bishops = [Bishop(WHITE) for _ in range(2)]
        self.black_knights = [Knight(BLACK) for _ in range(2)]
        self.white_knights = [Knight(WHITE) for _ in range(2)]
        self.black_queens = [Queen(BLACK)]
        self.white_queens = [Queen(WHITE)]
        self.black_kings = [King(BLACK)]
        self.white_kings = [King(WHITE)]
        self.black_pawns = [Pawn(BLACK) for _ in range(8)]
        self.white_pawns = [Pawn(WHITE) for _ in range(8)]

        self.white_pieces = [self.white_kings,
                             self.white_queens,
                             self.white_pawns,
                             self.white_rooks,
                             self.white_bishops,
                             self.white_knights]

        self.black_pieces = [self.black_kings,
                             self.black_queens,
                             self.black_pawns,
                             self.black_rooks,
                             self.black_bishops,
                             self.black_knights]

        self.teams = [self.black_pieces, self.white_pieces]

        self.board[0][0] = self.black_rooks[0]
        self.board[0][1] = self.black_knights[0]
        self.board[0][2] = self.black_bishops[0]
        self.board[0][3] = self.black_queens[0]
        self.board[0][4] = self.black_kings[0]
        self.board[0][5] = self.black_bishops[1]
        self.board[0][6] = self.black_knights[1]
        self.board[0][7] = self.black_rooks[1]

        for i in range(8):
            self.board[1][i] = self.black_pawns[i]
            self.board[6][i] = self.white_pawns[i]

        self.board[7][0] = self.white_rooks[0]
        self.board[7][1] = self.white_knights[0]
        self.board[7][2] = self.white_bishops[0]
        self.board[7][3] = self.white_queens[0]
        self.board[7][4] = self.white_kings[0]
        self.board[7][5] = self.white_bishops[1]
        self.board[7][6] = self.white_knights[1]
        self.board[7][7] = self.white_rooks[1]

        self.last_moved_piece = Empty()
        self.turn = WHITE

    def remove_piece(self, piece):
        for piecetype in self.teams[piece.color]:
            if piece in piecetype:
                piecetype.remove(piece)
                return

    def gets_blocked(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        dx = 1 - 2 * (x1 > x2)
        dy = 1 - 2 * (y1 > y2)

        if x1 == x2:
            return any([self[(x1, i)] for i in range(y1 + dy, y2 + dy, dy)])
        elif y1 == y2:
            return any([self[(i, y1)] for i in range(x1 + dx, x2 + dx, dx)])
        else:
            current = Coord(x1 + dx, y1 + dy)
            d = Coord(dx, dy)
            while current != Coord(x2, y2):
                if self[current]:
                    return True
                current += d
            return False

    def pawn_check(self, pos1, pos2):
        x1, y1 = pos1
        x2, _ = pos2

        # If no takes, only if spot is empty
        if x1 == x2:
            return not self[pos2]

        # If takes, if spot is full
        if self[pos2]:
            return True

        # Or if en passant
        if self[(x2, y1)] and self[(x2, y1)].en_passant:
            self.remove_piece(self[(x2, y1)])
            self[(x2, y1)] = Empty()
            return True

        return False


    def move(self, pos1, pos2):
        piece1 = self[pos1]
        piece2 = self[pos2]

        # Check both positions are valid
        if pos1 not in COORDINATES or pos2 not in COORDINATES:
            print('invalid coordinates')
            return

        # Check if there is a piece on pos1
        if not piece1:
            print('no piece to move')
            return

        if piece1.color != self.turn:
            print('not your turn')
            return

        # Check if the piece can make the move
        if pos2 not in {pos1 + move for move in piece1.potential_moves()}:
            print('illegal move, error code 1')
            return

        # Check if you move through another piece
        if not isinstance(piece1, Knight) and self.gets_blocked(pos1, pos2):
            print('illegal move, error code 2')
            return

        # Check special pawn rules
        if isinstance(piece1, Pawn) and not self.pawn_check(pos1, pos2):
            print('illegal move, error code 3')
            return

        if piece2:
            if piece2.color == piece1.color:
                print('cannot take own piece.')
                return
            self.remove_piece(piece2)

        self[pos2] = piece1
        self[pos1] = Empty()
        piece1.moved = True
        self.last_moved_piece.en_passant = False
        self.last_moved_piece = piece1
        if isinstance(piece1, Pawn) and abs((pos1 - pos2).y) == 2:
            piece1.en_passant = True
        self.turn = not self.turn

    def __repr__(self):
        background_colors = ('\033[43m', '\033[40m')
        string = ''
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                string += background_colors[(i + j) % 2] + ' ' + str(square) + ' \033[0;29;49m'
            string += '\n'
        return string[:-1]

    def __getitem__(self, coordinate: tuple):
        x, y = coordinate
        return self.board[y][x]

    def __setitem__(self, coordinate: tuple, piece: Piece):
        x, y = coordinate
        self.board[y][x] = piece
