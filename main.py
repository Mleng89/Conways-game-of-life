import time
from collections import defaultdict
from copy import deepcopy
import pygame
from grid import Grid, Neighbors, Dimension

pygame.init()

WIDTH, HEIGHT = 900, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (65, 105, 225)


"""
initalize class.method(WIDTH,HEIGHT,CELL/BLOCK_SIZE)
"""


# def draw_grid():
#     block_size = 100  # Set the size of the grid block
#     for x in range(0, WIDTH, block_size):  # (start, stop, step) === (0, 900/blocksize)
#         for y in range(0, HEIGHT, block_size):
#             rect = pygame.Rect(x, y, block_size, block_size)
#             pygame.draw.rect(WINDOW, WHITE, rect, 1)
def draw_grid(screen: pygame.Surface, grid: Grid) -> None:
    cell_width = screen.get_width() / grid.dimension.width
    cell_height = screen.get_height() / grid.dimension.height
    border_size = 2

    for (x, y) in grid.cells:
        pygame.draw.rect(
            screen,
            BLUE,
            (
                x * cell_width + border_size,
                y * cell_height + border_size,
                cell_width - border_size,
                cell_height - border_size,
            ),
        )


"""
Conway logic:

positions:
(-1,-1) (0,-1)(1,-1)

(-1,0)    X     (1,0)

(-1,1)  (0,1)  (1,1)

TODO:
- Alive or dead cells === 0 & 1? True or False?
     - Birth happens with 3 neighbors
     - Death happens with fewer than 2 or greater than 3

loop grid:
    loop each row:
        If (current cell's neighbors)
"""

# NEIGHBORS
direction = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def neighbors(grid: Grid, width, height):
    possible_neighbors = {
        (width + width_add, height + height_add) for width_add, height_add in direction
    }
    alive = {
        (position[0], position[1])
        for position in possible_neighbors
        if position in grid.cells
    }
    return Neighbors(alive, possible_neighbors - alive)


# Need to update grid
def update_grid(grid):
    new_cells = deepcopy(grid.cells)
    undead = defaultdict(int)
    for (x, y) in grid.cells:
        alive_neighbors, dead_neighbors = neighbors(grid, x, y)
        if len(alive_neighbors) not in [2, 3]:
            new_cells.remove((x, y))

        for position in dead_neighbors:
            undead[position] += 1

        for position, _ in filter(lambda element: element[1] == 3, undead.items()):
            new_cells.add((position[0], position[1]))
    return Grid(grid.dimension, new_cells)


def main():
    grid = Grid(
        Dimension(50, 50),
        {
            (22, 8),
            (22, 6),
            (22, 5),
            (22, 7),
        },
    )
    run = True
    # setting FPS to 60
    clock = pygame.time.Clock()
    clock.tick(60)
    WINDOW.fill(BLACK)

    while run:
        # cell = 30
        # g = Grid(WIDTH, HEIGHT, cell)
        # g.setup(WIDTH, HEIGHT, cell)
        # grid.draw_grid()  # init class.method(WIDTH, HEIGHT, cell, WINDOW)
        # Following loop is required or else pygame will freeze.
        for event in pygame.event.get():
            # print("what are events", event)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_grid(WINDOW, grid)
        grid = update_grid(grid)
        pygame.display.flip()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
