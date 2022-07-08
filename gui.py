import pygame as pg
import os

WIDTH = 512
HEIGHT = 512

SQUARE_W = WIDTH / 8
SQUARE_H = HEIGHT / 8

FPS = 60

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Chess")

WHITE = (255, 255, 255)
BG_COLOR = (190, 190, 190)

BOARD_COLORS = ((245, 179, 66), (99, 70, 21))

KING_BLACK_IMAGE = pg.image.load(os.path.join('Assets', 'king_black.png'))
KING_WHITE_IMAGE = pg.image.load(os.path.join('Assets', 'king_white.png'))
QUEEN_BLACK_IMAGE = pg.image.load(os.path.join('Assets', 'queen_black.png'))
QUEEN_WHITE_IMAGE = pg.image.load(os.path.join('Assets', 'queen_white.png'))
ROOK_BLACK_IMAGE = pg.image.load(os.path.join('Assets', 'rook_black.png'))
ROOK_WHITE_IMAGE = pg.image.load(os.path.join('Assets', 'rook_white.png'))
BISHOP_BLACK_IMAGE = pg.image.load(os.path.join('Assets', 'bishop_black.png'))
BISHOP_WHITE_IMAGE = pg.image.load(os.path.join('Assets', 'bishop_white.png'))
KNIGHT_BLACK_IMAGE = pg.image.load(os.path.join('Assets', 'knight_black.png'))
KNIGHT_WHITE_IMAGE = pg.image.load(os.path.join('Assets', 'knight_white.png'))
PAWN_BLACK_IMAGE = pg.image.load(os.path.join('Assets', 'pawn_black.png'))
PAWN_WHITE_IMAGE = pg.image.load(os.path.join('Assets', 'pawn_white.png'))

KING_BLACK = pg.transform.scale(KING_BLACK_IMAGE, (WIDTH / 8, HEIGHT / 8))
KING_WHITE = pg.transform.scale(KING_WHITE_IMAGE, (WIDTH / 8, HEIGHT / 8))
QUEEN_BLACK = pg.transform.scale(QUEEN_BLACK_IMAGE, (WIDTH / 8, HEIGHT / 8))
QUEEN_WHITE = pg.transform.scale(QUEEN_WHITE_IMAGE, (WIDTH / 8, HEIGHT / 8))
ROOK_BLACK = pg.transform.scale(ROOK_BLACK_IMAGE, (WIDTH / 8, HEIGHT / 8))
ROOK_WHITE = pg.transform.scale(ROOK_WHITE_IMAGE, (WIDTH / 8, HEIGHT / 8))
KNIGHT_BLACK = pg.transform.scale(KNIGHT_BLACK_IMAGE, (WIDTH / 8, HEIGHT / 8))
KNIGHT_WHITE = pg.transform.scale(KNIGHT_WHITE_IMAGE, (WIDTH / 8, HEIGHT / 8))
BISHOP_BLACK = pg.transform.scale(BISHOP_BLACK_IMAGE, (WIDTH / 8, HEIGHT / 8))
BISHOP_WHITE = pg.transform.scale(BISHOP_WHITE_IMAGE, (WIDTH / 8, HEIGHT / 8))
PAWN_BLACK = pg.transform.scale(PAWN_BLACK_IMAGE, (WIDTH / 8, HEIGHT / 8))
PAWN_WHITE = pg.transform.scale(PAWN_WHITE_IMAGE, (WIDTH / 8, HEIGHT / 8))

id_to_image = {
    'kb': KING_BLACK,
    'kw': KING_WHITE,
    'qb': QUEEN_BLACK,
    'qw': QUEEN_WHITE,
    'rb': ROOK_BLACK,
    'rw': ROOK_WHITE,
    'nb': KNIGHT_BLACK,
    'nw': KNIGHT_WHITE,
    'bb': BISHOP_BLACK,
    'bw': BISHOP_WHITE,
    'pb': PAWN_BLACK,
    'pw': PAWN_WHITE
}
