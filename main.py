import pygame
from grid import Grid

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


def draw_grid():
    block_size = 100  # Set the size of the grid block
    for x in range(0, WIDTH, block_size):  # (start, stop, step) === (0, 900/blocksize)
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(WINDOW, WHITE, rect, 1)


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


def main():
    run = True
    # setting FPS to 60
    clock = pygame.time.Clock()
    clock.tick(60)
    WINDOW.fill(BLACK)
    while run:
        # cell = 30
        draw_grid()
        # g = Grid(WIDTH, HEIGHT, cell)
        # g.setup(WIDTH, HEIGHT, cell)
        # grid.draw_grid()  # init class.method(WIDTH, HEIGHT, cell, WINDOW)
        # Following loop is required or else pygame will freeze.
        for event in pygame.event.get():
            # print("what are events", event)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        pygame.display.flip()


main()
