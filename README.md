# Conway's Game of Life

### Requirements / Rules:

1. Any live cell with fewer than 2 live neighbor dies, as if by underpopulation.
2. Any live cell with 2 or 3 live neighbors lives on to the next generation.
3. Any live cell with more than 3 live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly 3 live neighbors becomes a live cell, as if by reproduction.

#### Condensed rules:

1. Any live cell with 2 or 3 live neighbors survives.
2. Any dead cell with 3 live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

🛠️ [Requirements/Rules obtained from Wiki](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules)

## Start up on local machine:

### In terminal:

1. `python -m venv <Name-of-your-choice>` or `python3 -m venv <Name-of-your-choice>` (to create a virtual environment to install pygame)
2. `source <Name-of-your-venv-folder>/bin/activate` (spins up your virtual environment)
3. `pip install pygame`

### Starting pygame:

4. While still in virtual environment, type `python main.py` into your terminal.
