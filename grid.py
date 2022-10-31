from collections import namedtuple

Dimension = namedtuple("Dimension", ["width", "height"])
Grid = namedtuple("Grid", ["dimension", "cells"])
Neighbors = namedtuple("Neighbors", ["alive", "dead"])


"""
TODO:
- 2D list
    - colums, rows

Neighborhood:
[ ][ ][ ]
[ ][x][ ]
[ ][ ][ ]
"""


# class Grid:
#     def __init__(self, width, height, cells):
#         self.height = height
#         self.width = width
#         self.cells = cells
# self.window = window

# def make_list(self):
#     for x in range(self.width):
#         for y in range(self.height):
#             pass

# def setup(self, width, height, cells=30):
#     window = pygame.display.set_mode(width, height)
#     for x in range(0, width, cells):
#         for y in range(0, height, cells):
#             rect = pygame.Rect(x, y, cells, cells)
#             pygame.draw.rect(window, (255, 255, 255), rect, 1)
