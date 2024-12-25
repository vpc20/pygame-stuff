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
cols = WIDTH // LINE_LEN
rows = HEIGHT // LINE_LEN
# print(WIDTH, HEIGHT)
print(cols, rows)

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
    def dfs(row, col):
        visited.add((row, col))
        rc_delta = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        random.shuffle(rc_delta)
        for r, c in rc_delta:
            if 0 < r <= rows and 0 < c < cols:
                if (r, c) not in visited:
                    if len(visited) < vcount:
                        pg.draw.line(screen, DARKGRAY, (col * LINE_LEN, row * LINE_LEN), (c * LINE_LEN, r * LINE_LEN))
                        pg.time.delay(32)
                        pg.display.flip()  # Update the full display Surface to the screen
                        dfs(r, c)

    visited = set()
    vcount = rows * cols
    dfs(1, 1)


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
