import random
import sys

import pygame as pg

sys.setrecursionlimit(10 ** 6)

# WIDTH = 1280
# HEIGHT = 600
# WIDTH = 640
# HEIGHT = 300
WIDTH = 1280
HEIGHT = 720
LINE_LEN = 8

# CELL_WIDTH = 8
# CELL_HEIGHT = CELL_WIDTH

BLACK = pg.Color('black')
DARKGRAY = pg.Color('darkgray')

pg.init()
ncols = WIDTH // LINE_LEN
nrows = HEIGHT // LINE_LEN
# print(WIDTH, HEIGHT)
print(ncols, nrows)

screen = pg.display.set_mode((WIDTH, HEIGHT))  # screen is a pg.Surface object
pg.display.set_caption("Maze Generator")
pg.display.set_icon(pg.image.load('robot-128.png'))


# grid = [[0] * cols for _ in range(rows)]


# def draw_grid():
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == 1:
#                 pg.draw.rect(screen, DARKGRAY, pg.Rect(j * CELL_WIDTH, i * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
#             else:
#                 pg.draw.rect(screen, BLACK, pg.Rect(j * CELL_WIDTH, i * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))


def update_grid():
    visited = set()
    visited.add((1, 1))

    for r in range(1, nrows):
        for c in range(1, ncols):
            rc_delta = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
            choi = random.choices(rc_delta, k=4)
            for nr, nc in choi:
                if 0 < nr < nrows and 0 < nc < ncols and (nr, nc) not in visited:
                    pg.draw.line(screen, DARKGRAY, (c * LINE_LEN, r * LINE_LEN), (nc * LINE_LEN, nr * LINE_LEN))
                    pg.time.delay(1)
                    pg.display.flip()  # Update the full display Surface to the screen
                    visited.add((nr, nc))

    # for r in range(1, nrows):
    #     for c in range(1, ncols):
    #         rc_delta = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
    #         nr, nc = random.choice(rc_delta)
    #         if 0 < nr < nrows and 0 < nc < ncols and (nr, nc) not in visited:
    #             pg.draw.line(screen, DARKGRAY, (c * LINE_LEN, r * LINE_LEN), (nc * LINE_LEN, nr * LINE_LEN))
    #             pg.time.delay(20)
    #             pg.display.flip()  # Update the full display Surface to the screen
    #             visited.add((nr, nc))
    #


update_grid()
paused = False
while True:
    pass
# while True:
#     e = pg.event.poll()  # get a single event from the queue
#     if e.type == pg.QUIT:
#         break
#
#     keys = pg.key.get_pressed()
#     if keys[pg.K_ESCAPE]:
#         break
#     elif keys[pg.K_F3]:
#         paused = not paused
#     # elif keys[pg.K_F4]:
#     #     paused = False
#     # elif keys[pg.K_F5]:
#     #     for row in range(rows):
#     #         for col in range(cols):
#     #             grid[row][col] = 0
#     #     draw_grid()
#     #     pg.display.flip()  # Update the full display Surface to the screen
#
#     # if pg.mouse.get_pressed() == (1, 0, 0):
#     #     col, row = pg.mouse.get_pos()
#     #     col = col // CELL_WIDTH
#     #     row = row // CELL_WIDTH
#     #     if grid[row][col] == 0:
#     #         pg.draw.rect(screen, DARKGRAY,
#     #                      pg.Rect(col * CELL_WIDTH, row * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
#     #     else:
#     #         pg.draw.rect(screen, BLACK,
#     #                      pg.Rect(col * CELL_WIDTH, row * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
#     #
#     #     grid[row][col] = 1 - grid[row][col]
#     #     pg.display.update()
#
#     if not paused:
#         # update_grid()
#         pg.display.flip()  # Update the full display Surface to the screen

pg.quit()
