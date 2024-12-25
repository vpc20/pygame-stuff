import sys

import pygame

# Constants
WINDOW_SIZE = 800
FPS = 30
CELL_SIZE = 30

# Colors
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 255)
START_COLOR = (0, 255, 0)
END_COLOR = (255, 0, 0)
VISITED_COLOR = (0, 0, 255)
SOLUTION_COLOR = (255, 255, 0)


# Load maze from file
def load_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze


# Draw the maze
def draw_maze(screen, maze, visited, path):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = PATH_COLOR
            if cell == '#':
                color = WALL_COLOR
            elif cell == 'S':
                color = START_COLOR
            elif cell == 'E':
                color = END_COLOR
            elif (x, y) in path:
                color = SOLUTION_COLOR
            elif (x, y) in visited:
                color = VISITED_COLOR
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (200, 200, 200), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


# Find the start and end positions
def find_positions(maze):
    start = end = None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return start, end


# DFS recursive function to solve the maze
def dfs(screen, maze, x, y, end, visited, path):
    if (x, y) == end:
        path.append((x, y))
        return True

    visited.add((x, y))
    draw_maze(screen, maze, visited, path)
    pygame.display.flip()
    pygame.time.delay(250)

    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] != '#' and (nx, ny) not in visited:
            if dfs(screen, maze, nx, ny, end, visited, path):
                path.append((x, y))
                return True

    return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Maze Solver Visualization")

    maze = load_maze('maze_small.txt')
    start, end = find_positions(maze)

    visited = set()
    path = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))
        draw_maze(screen, maze, visited, path)
        pygame.display.flip()

        if start and end:
            dfs(screen, maze, *start, end, visited, path)
            start = None  # To ensure DFS runs only once

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
