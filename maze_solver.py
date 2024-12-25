import pygame as pg


def draw_maze():
    nrows, ncols = len(maze), len(maze[0])
    for r in range(nrows):
        for c in range(ncols):
            if maze[r][c] == '#':
                pg.draw.rect(screen, BLACK, pg.Rect(c * CELL_WIDTH, r * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
            elif maze[r][c] == 'S':
                pg.draw.rect(screen, BLUE, pg.Rect(c * CELL_WIDTH, r * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
                start = (r, c)
            elif maze[r][c] == 'E':
                pg.draw.rect(screen, RED, pg.Rect(c * CELL_WIDTH, r * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
                end = (r, c)
            else:
                pg.draw.rect(screen, WHITE, pg.Rect(c * CELL_WIDTH, r * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
    return start, end


def update_maze():
    nrows, ncols = len(maze), len(maze[0])
    visited = set()
    stack = [(start, [])]

    while stack:
        (r, c), path = stack.pop()

        if (r, c) == end:
            return path + [(r, c)]

        visited.add((r, c))

        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1), ]:
            if 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in visited and maze[nr][
                nc] in ('.', 'E'):
                stack.append(((nr, nc), path + [(r, c)]))
                pg.draw.rect(screen, GREEN, pg.Rect(nc * CELL_WIDTH, nr * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
                pg.display.flip()  # Update the full display Surface to the screen
                pg.time.delay(100)
        # pg.draw.rect(screen, WHITE, pg.Rect(c * CELL_WIDTH, r * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
        # pg.display.flip()  # Update the full display Surface to the screen
        pg.time.delay(100)


    return None


def show_path(path):
    for r, c in path:
        pg.draw.rect(screen, GREEN, pg.Rect(c * CELL_WIDTH, r * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
        pg.display.flip()  # Update the full display Surface to the screen
        pg.time.delay(100)


f = open('maze_small.txt')
maze = [[c for c in s.strip()] for s in f]
f.close()

# for e in maze:
#     print(e)

WIDTH = 720
HEIGHT = 720

nrows = len(maze)
ncols = len(maze[0])

CELL_HEIGHT = HEIGHT // nrows
CELL_WIDTH = CELL_HEIGHT

# CELL_WIDTH = 32
# CELL_HEIGHT = CELL_WIDTH

# WIDTH = CELL_WIDTH * ncols
# HEIGHT = CELL_HEIGHT * nrows

BLACK = pg.Color('black')
DARKGRAY = pg.Color('darkgray')
LIGHTGRAY = pg.Color('lightgray')
WHITE = pg.Color('white')
BLUE = pg.Color('blue')
GREEN = pg.Color('green')
RED = pg.Color('red')

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))  # screen is a pg.Surface object
pg.display.set_caption("Maze")
pg.display.set_icon(pg.image.load('robot-128.png'))

start, end = draw_maze()
paused = False

while True:
    e = pg.event.poll()  # get a single event from the queue
    if e.type == pg.QUIT:
        break

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        break
    # elif keys[pg.K_F3]:
    #     paused = True
    # elif keys[pg.K_F4]:
    #     paused = False
    # elif keys[pg.K_F5]:
    #     for row in range(nrows):
    #         for col in range(ncols):
    #             maze[row][col] = 0
    #     draw_maze()
    #     pg.display.flip()  # Update the full display Surface to the screen

    # if pg.mouse.get_pressed() == (1, 0, 0):
    #     col, row = pg.mouse.get_pos()
    #     col = col // CELL_WIDTH
    #     row = row // CELL_WIDTH
    #     if maze[row][col] == 0:
    #         pg.draw.rect(screen, DARKGRAY,
    #                      pg.Rect(col * CELL_WIDTH, row * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
    #     else:
    #         pg.draw.rect(screen, BLACK,
    #                      pg.Rect(col * CELL_WIDTH, row * CELL_WIDTH, CELL_WIDTH, CELL_HEIGHT))
    #
    #     maze[row][col] = 1 - maze[row][col]
    #     pg.display.update()

    path = update_maze()
    start, end = draw_maze()
    pg.display.flip()  # Update the full display Surface to the screen
    show_path(path[1:len(path) - 1])
    pg.display.flip()  # Update the full display Surface to the screen
    pg.time.delay(100000)

pg.quit()
