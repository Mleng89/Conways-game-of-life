"""
TODO:
- 2D list
    - colums, rows

Neighborhood:
[ ][ ][ ]
[ ][x][ ]
[ ][ ][ ]
"""


class Grid:
    def __init__(self, width, height, cells):
        self.columns = height
        self.rows = width

    def make_list(self):
        for x in range(self.rows):
            for y in range(self.columns):
                pass

    def setup(self):
        # grid = make_list(10, 10)
        pass
