import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
from coordinates import *
from gui import *
from board import *

def draw_background():
    for i in range(8):
        for j in range(8):
            pg.draw.rect(WIN, BOARD_COLORS[(i+j) % 2], pg.Rect(i*SQUARE_W, j*SQUARE_H, (i+1)*SQUARE_W, (j+1)*SQUARE_H))

def draw_piece(piece_id, pos):
    img = id_to_image[piece_id]
    x, y = pos
    WIN.blit(img, (SQUARE_W*x, SQUARE_H*y))

def draw_board(b):
    for y, row in enumerate(b.board):
        for x, piece in enumerate(row):
            if piece:
                draw_piece(piece.id, (x, y))

def draw_window(b):
    WIN.fill(BG_COLOR)
    draw_background()
    draw_board(b)
    pg.display.update()

def click(b: Board, selected: Coord):
    x, y = pg.mouse.get_pos()
    pos = Coord(int(x / SQUARE_W), int(y / SQUARE_H))
    if selected:
        b.move(selected, pos)
        return
    return pos


def main():
    clock = pg.time.Clock()

    b = Board()
    selected = None

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_presses = pg.mouse.get_pressed()
                if mouse_presses[0]:
                    selected = click(b, selected)

        draw_window(b)

    pg.quit()


if __name__ == '__main__':
    main()