from numpy import isin
from coordinates import *
from pieces import *

class Board:
    def __init__(self):
        self.board = [[Empty() for _ in range(8)] for _ in range(8)]

        self.board[0][0] = Rook(BLACK, a8)
        self.board[0][1] = Knight(BLACK, b8)
        self.board[0][2] = Bishop(BLACK, c8)
        self.board[0][3] = Queen(BLACK, d8)
        self.board[0][4] = black_king = King(BLACK, e8)
        self.board[0][5] = Bishop(BLACK, f8)
        self.board[0][6] = Knight(BLACK, g8)
        self.board[0][7] = Rook(BLACK, h8)

        for i in range(8):
            self.board[1][i] = Pawn(BLACK, Coord(1, i))
            self.board[6][i] = Pawn(WHITE, Coord(6, i))

        self.board[7][0] = Rook(WHITE, a1)
        self.board[7][1] = Knight(WHITE, b1)
        self.board[7][2] = Bishop(WHITE, c1)
        self.board[7][3] = Queen(WHITE, d1)
        self.board[7][4] = white_king = King(WHITE, e1)
        self.board[7][5] = Bishop(WHITE, f1)
        self.board[7][6] = Knight(WHITE, g1)
        self.board[7][7] = Rook(WHITE, h1)

        self.kings = (black_king, white_king)

        self.black_pieces = [self.board[i][j] for i in range(2) for j in range(8)]
        self.white_pieces = [self.board[i][j] for i in range(6, 8) for j in range(8)]

        self.teams = (self.black_pieces, self.white_pieces)

        self.last_moved_piece = Empty()
        self.turn = WHITE

    def remove_piece(self, piece):
        team = self.teams[piece.color]
        for piece in team:
            team.remove(piece)
            return

    def in_check(self, pos, enemy):
        enemy_pieces = self.teams[enemy]
        # print(enemy_pieces)
        # [print(p, p.pos, pos, self.is_valid(p.pos, pos)) for p in enemy_pieces]
        return any([self.is_valid(p.pos, pos)[0] for p in enemy_pieces])

    def gets_blocked(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        dx = 1 - 2 * (x1 > x2)
        dy = 1 - 2 * (y1 > y2)

        if x1 == x2:
            return any([self[(x1, i)] for i in range(y1 + dy, y2, dy)])
        elif y1 == y2:
            return any([self[(i, y1)] for i in range(x1 + dx, x2, dx)])
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
            return 'en passant'

        return False


    def is_valid(self, pos1, pos2, verbose=False):
        '''Returns if the move is valid and if its en passant.'''
        piece1 = self[pos1]
        piece2 = self[pos2]

        # Check both positions are valid
        if pos1 not in COORDINATES or pos2 not in COORDINATES:
            if verbose: print('invalid coordinates')
            return False, False

        # Check if there is a piece on pos1
        if not piece1:
            if verbose: print('no piece to move')
            return False, False

        if piece1.color != self.turn:
            if verbose: print('not your turn')
            return False, False

        # Check if the piece can make the move
        if pos2 not in {pos1 + move for move in piece1.potential_moves()}:
            if verbose: print('illegal move')
            return False, False

        # Check if you move through another piece
        if not isinstance(piece1, Knight) and self.gets_blocked(pos1, pos2):
            if verbose: print('cannot move through another piece')
            return False, False

        # Check special pawn rules
        pawn_move = self.pawn_check(pos1, pos2)
        if isinstance(piece1, Pawn) and not pawn_move:
            if verbose: print('illegal pawn move')
            return False, False

        if piece2 and piece2.color == piece1.color:
            if verbose: print('cannot take own piece.')
            return False, False

        return True, pawn_move

    def move(self, pos1, pos2):
        piece1 = self[pos1]
        piece2 = self[pos2]

        valid, pawn_move = self.is_valid(pos1, pos2, verbose=True)

        if not valid:
            return

        if pawn_move == 'en passant':
            pos3 = (pos2.x, pos1.y)
            piece2 = self[pos3]
            self[pos3] = Empty()

        if piece2:
            self.remove_piece(piece2)

        piece1.pos = pos2
        self[pos2] = piece1
        self[pos1] = Empty()

        # backup
        moved = piece1.moved
        last_en_passant = self.last_moved_piece.en_passant
        last_moved_piece = self.last_moved_piece
        en_passant = piece1.en_passant

        piece1.moved = True
        self.last_moved_piece.en_passant = False
        self.last_moved_piece = piece1
        if isinstance(piece1, Pawn) and abs((pos1 - pos2).y) == 2:
            piece1.en_passant = True

        self.turn = not self.turn

        if self.in_check(self.kings[not self.turn].pos, self.turn):
            if piece2:
                self.teams[self.turn].append(piece2)
            piece1.pos = pos1
            self[pos2] = piece2
            self[pos1] = piece1
            piece1.moved = moved
            self.last_moved_piece.en_passant = last_en_passant
            self.last_moved_piece = last_moved_piece
            piece1.en_passant = en_passant
            self.turn = not self.turn
            print('cannot move into check')
            return

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
