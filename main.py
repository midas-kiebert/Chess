from asyncore import loop
from coordinates import *
import pieces
import board

b = board.Board()
print(b)
while 1:
    pos1, pos2 = input('>>> ').split()

    pos1 = COORDINATES_DICT[pos1]
    pos2 = COORDINATES_DICT[pos2]

    b.move(pos1, pos2)
    print(b)