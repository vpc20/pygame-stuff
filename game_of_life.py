from random import randint

import pygame as pg

WIDTH = 1280
HEIGHT = 600

CELL_WIDTH = 8
CELL_HEIGHT = CELL_WIDTH

BLACK = pg.Color('black')
DARKGRAY = pg.Color('darkgray')

pg.init()
cols = WIDTH // CELL_WIDTH
rows = HEIGHT // CELL_HEIGHT
print(WIDTH, HEIGHT)
print(cols, rows)

screen = pg.display.set_mode((WIDTH, HEIGHT))  # screen is a pg.Surface object
pg.display.set_caption("Conway's Game of Life")
pg.display.set_icon(pg.image.load('robot-128.png'))

grid = [[0] * cols for _ in range(rows)]

# blinker
# grid[2][3] = 1
# grid[2][4] = 1
# grid[2][5] = 1


# grid[1][2] = 1
# grid[1][3] = 1
# grid[1][4] = 1
# grid[2][3] = 1
# grid[2][4] = 1
# grid[2][5] = 1

# beacon
# grid[1][2] = 1
# grid[1][3] = 1
# grid[2][2] = 1
# grid[2][3] = 1
# grid[3][4] = 1
# grid[3][5] = 1
# grid[4][4] = 1
# grid[4][5] = 1

# r-pentomino
# grid[2][6] = 1
# grid[2][7] = 1
# grid[3][5] = 1
# grid[3][6] = 1
# grid[4][6] = 1

# glider
# grid[3][3] = 1
# grid[3][4] = 1
# grid[3][5] = 1
# grid[2][5] = 1
# grid[1][4] = 1

# spaceship
# grid[8][110] = 1
# grid[8][111] = 1
# grid[8][112] = 1
# grid[8][113] = 1
# grid[6][110] = 1
# grid[7][110] = 1
# grid[5][111] = 1
# grid[7][114] = 1
# grid[5][114] = 1

# random grid generator
for i in range(rows):
    for j in range(cols):
        if randint(0, 4) == 0:
            grid[i][j] = 1


def draw_grid():
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                pg.draw.rect(screen, DARKGRAY, pg.Rect(j * CELL_WIDTH, i * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
            else:
                pg.draw.rect(screen, BLACK, pg.Rect(j * CELL_WIDTH, i * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))


def update_grid():
    pg.time.delay(300)
    draw_grid()

    # for some reason, grid_copy = grid.copy() does not work
    # grid_copy = grid[:] # slicing does not work
    # grid_copy = [e for e in grid]  # list comprehension also does not work
    # grid_copy = [grid[row] for row in range(ROWS)]  # list comprehension also does not work
    grid_copy = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            grid_copy[row][col] = grid[row][col]

    # update cells based on life rules
    for row in range(rows):
        for col in range(cols):
            count = 0  # neighbor count
            for newrow, newcol in ([(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col + 1),
                                    (row + 1, col + 1), (row + 1, col), (row + 1, col - 1), (row, col - 1)]):
                if -1 < newrow < rows and -1 < newcol < cols:
                    if grid_copy[newrow][newcol] == 1:
                        count += 1
            if grid_copy[row][col] == 1:
                if count < 2 or count > 3:
                    grid[row][col] = 0
            else:
                if count == 3:
                    grid[row][col] = 1


paused = False
while True:
    e = pg.event.poll()  # get a single event from the queue
    if e.type == pg.QUIT:
        break

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        break
    elif keys[pg.K_F3]:
        paused = True
    elif keys[pg.K_F4]:
        paused = False
    elif keys[pg.K_F5]:
        for row in range(rows):
            for col in range(cols):
                grid[row][col] = 0
        draw_grid()
        pg.display.flip()  # Update the full display Surface to the screen

    if pg.mouse.get_pressed() == (1, 0, 0):
        col, row = pg.mouse.get_pos()
        col = col // CELL_WIDTH
        row = row // CELL_WIDTH
        if grid[row][col] == 0:
            pg.draw.rect(screen, DARKGRAY,
                         pg.Rect(col * CELL_WIDTH, row * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
        else:
            pg.draw.rect(screen, BLACK,
                         pg.Rect(col * CELL_WIDTH, row * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))

        grid[row][col] = 1 - grid[row][col]
        pg.display.update()

    if not paused:
        update_grid()
        pg.display.flip()  # Update the full display Surface to the screen

pg.quit()
