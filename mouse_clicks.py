import time
from random import randint

import pygame

# BORDER = 20

GRID_HEIGHT = 5
GRID_WIDTH = 5

ROWS = 120
COLS = 240

HEIGHT = ROWS * GRID_WIDTH
WIDTH = COLS * GRID_WIDTH

BLACK = pygame.Color('black')
DARKGRAY = pygame.Color('darkgray')

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # screen is a pygame.Surface object

grid = [[0] * COLS for _ in range(ROWS)]

while True:
    e = pygame.event.poll()  # get a single event from the queue
    if e.type == pygame.QUIT:
        break

    if pygame.mouse.get_pressed() == (1, 0, 0):
        x, y = pygame.mouse.get_pos()
        print(x, y)
        x = x // GRID_WIDTH
        y = y // GRID_WIDTH
        print(x, y)

        pygame.draw.rect(screen, DARKGRAY,
                         pygame.Rect(x * GRID_WIDTH, y * GRID_WIDTH, GRID_WIDTH, GRID_HEIGHT))

    pygame.display.flip()  # Update the full display Surface to the screen

pygame.quit()
