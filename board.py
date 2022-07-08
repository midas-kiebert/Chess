from pieces import *

class Board:
    SIZE = 8

    def __init__(self):
        self.board = Board.generate_board()

    @staticmethod
    def generate_board():
        board = [[' ' for _ in range(Board.SIZE)] for _ in range(Board.SIZE)]
        board[0][0] = Rook(BLACK)
        board[0][1] = Knight(BLACK)
        board[0][2] = Bishop(BLACK)
        board[0][3] = Queen(BLACK)
        board[0][4] = King(BLACK)
        board[0][5] = Bishop(BLACK)
        board[0][6] = Knight(BLACK)
        board[0][7] = Rook(BLACK)

        for i in range(8):
            board[1][i] = Pawn(BLACK)
            board[6][i] = Pawn(WHITE)

        board[7][0] = Rook(WHITE)
        board[7][1] = Knight(WHITE)
        board[7][2] = Bishop(WHITE)
        board[7][3] = Queen(WHITE)
        board[7][4] = King(WHITE)
        board[7][5] = Bishop(WHITE)
        board[7][6] = Knight(WHITE)
        board[7][7] = Rook(WHITE)

        return board

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
