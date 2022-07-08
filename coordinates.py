class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __iter__(self):
        return iter((self.x, self.y))

    def __repr__(self):
        return f'({str(self.x)}, {str(self.y)})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


a8 = Coord(0, 0)
a7 = Coord(0, 1)
a6 = Coord(0, 2)
a5 = Coord(0, 3)
a4 = Coord(0, 4)
a3 = Coord(0, 5)
a2 = Coord(0, 6)
a1 = Coord(0, 7)

b8 = Coord(1, 0)
b7 = Coord(1, 1)
b6 = Coord(1, 2)
b5 = Coord(1, 3)
b4 = Coord(1, 4)
b3 = Coord(1, 5)
b2 = Coord(1, 6)
b1 = Coord(1, 7)

c8 = Coord(2, 0)
c7 = Coord(2, 1)
c6 = Coord(2, 2)
c5 = Coord(2, 3)
c4 = Coord(2, 4)
c3 = Coord(2, 5)
c2 = Coord(2, 6)
c1 = Coord(2, 7)

d8 = Coord(3, 0)
d7 = Coord(3, 1)
d6 = Coord(3, 2)
d5 = Coord(3, 3)
d4 = Coord(3, 4)
d3 = Coord(3, 5)
d2 = Coord(3, 6)
d1 = Coord(3, 7)

e8 = Coord(4, 0)
e7 = Coord(4, 1)
e6 = Coord(4, 2)
e5 = Coord(4, 3)
e4 = Coord(4, 4)
e3 = Coord(4, 5)
e2 = Coord(4, 6)
e1 = Coord(4, 7)

f8 = Coord(5, 0)
f7 = Coord(5, 1)
f6 = Coord(5, 2)
f5 = Coord(5, 3)
f4 = Coord(5, 4)
f3 = Coord(5, 5)
f2 = Coord(5, 6)
f1 = Coord(5, 7)

g8 = Coord(6, 0)
g7 = Coord(6, 1)
g6 = Coord(6, 2)
g5 = Coord(6, 3)
g4 = Coord(6, 4)
g3 = Coord(6, 5)
g2 = Coord(6, 6)
g1 = Coord(6, 7)

h8 = Coord(7, 0)
h7 = Coord(7, 1)
h6 = Coord(7, 2)
h5 = Coord(7, 3)
h4 = Coord(7, 4)
h3 = Coord(7, 5)
h2 = Coord(7, 6)
h1 = Coord(7, 7)

COORDINATES = {
    a8, b8, c8, d8, e8, f8, g8, h8,
    a7, b7, c7, d7, e7, f7, g7, h7,
    a6, b6, c6, d6, e6, f6, g6, h6,
    a5, b5, c5, d5, e5, f5, g5, h5,
    a4, b4, c4, d4, e4, f4, g4, h4,
    a3, b3, c3, d3, e3, f3, g3, h3,
    a2, b2, c2, d2, e2, f2, g2, h2,
    a1, b1, c1, d1, e1, f1, g1, h1
}

COORDINATES_DICT = {
    'a8': a8, 'b8': b8, 'c8': c8, 'd8': d8, 'e8': e8, 'f8': f8, 'g8': g8, 'h8': h8,
    'a7': a7, 'b7': b7, 'c7': c7, 'd7': d7, 'e7': e7, 'f7': f7, 'g7': g7, 'h7': h7,
    'a6': a6, 'b6': b6, 'c6': c6, 'd6': d6, 'e6': e6, 'f6': f6, 'g6': g6, 'h6': h6,
    'a5': a5, 'b5': b5, 'c5': c5, 'd5': d5, 'e5': e5, 'f5': f5, 'g5': g5, 'h5': h5,
    'a4': a4, 'b4': b4, 'c4': c4, 'd4': d4, 'e4': e4, 'f4': f4, 'g4': g4, 'h4': h4,
    'a3': a3, 'b3': b3, 'c3': c3, 'd3': d3, 'e3': e3, 'f3': f3, 'g3': g3, 'h3': h3,
    'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2, 'f2': f2, 'g2': g2, 'h2': h2,
    'a1': a1, 'b1': b1, 'c1': c1, 'd1': d1, 'e1': e1, 'f1': f1, 'g1': g1, 'h1': h1,
}