from pieces import *

class Board:
    SIZE = 8

    def __init__(self):
        self.board = Board.generate_board()

    @staticmethod
    def generate_board():
        board = [[' ' for _ in range(Board.SIZE)] for _ in range(Board.SIZE)]
        board[0][0] = Rook(Piece.BLACK)
        return board

    def __repr__(self):
        string = ''
        for row in self.board:
            for square in row:
                string += str(square) + ' '
            string = string[:-1]
            string += '\n'
        return string[:-1]

    def __getitem__(self, coordinate: tuple):
        x, y = coordinate
        return self.board[y][x]
