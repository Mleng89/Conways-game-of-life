import pygame
import grid

pygame.init()

WIDTH, HEIGHT = 900, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (65, 105, 225)

"""
TODO:
- Alive or dead cells === 0 & 1? True or False?
    - Birth happens with 3 neighbors
    - Death happens with fewer than 2 or greater than 3
"""


def main():
    run = True
    # setting FPS to 60
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        WINDOW.fill((0, 0, 0))
        # Following loop is required or else pygame will freeze.
        for event in pygame.event.get():
            # print("what are events", event)
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()
