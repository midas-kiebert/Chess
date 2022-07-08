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

    def remove_piece(self, piece):
        for team in self.teams:
            for piecetype in team:
                if piece in piecetype:
                    piecetype.remove(piece)

    def move(self, pos1, pos2):
        piece1 = self[pos1]
        piece2 = self[pos2]

        # Check if legal

        if piece2:
            self.remove_piece(piece2)

        self[pos2] = piece1
        self[pos1] = Empty()

        print(self)

    def __repr__(self):
        background_colors = ('\033[43m', '\033[40m')
        string = ''
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                string += background_colors[(i + j) % 2] + ' ' + str(square) + ' \033[49m'
            string += '\n'
        return string[:-1]

    def __getitem__(self, coordinate: tuple):
        x, y = coordinate
        return self.board[y][x]

    def __setitem__(self, coordinate: tuple, piece: Piece):
        x, y = coordinate
        self.board[y][x] = piece
