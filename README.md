# Conway's Game of Life

This is a simple implementation of Conway's Game of Life written in Python using the pygame library. The game is based on a cellular automaton that simulates the evolution of cells with simple rules.

# Description

Conway's Game of Life was originally designed by mathematician John Conway in 1970. It is a cellular automaton in which cells on a grid can either be alive or dead. The next generation of cells is computed based on the current state of the grid and the following rules:

1. A live cell with 2 or 3 live neighbors remains alive.
2. A dead cell with exactly 3 live neighbors becomes alive.
3. In all other cases, a cell dies or remains dead.

In this implementation, you can manually place cells on the grid and then run the simulation to observe their evolution.

# Features

1. Draw cells by clicking or dragging the mouse.
2. Randomly generate the initial grid.
3. Start and pause the simulation.
4. Reset and clear the grid.
5. Simple interface using the pygame library.

# Installation

### Install dependencies

```
pip install pygame
```

### Run the game

```
python life.py
```

# Controls

```Space``` - Start/Pause the simulation.
```S``` - Randomly populate the grid with cells.
```R``` - Reset the grid (clear all cells).
```Left Mouse Button (click)``` - Place or remove a cell on the grid.
```Left Mouse Button (drag)``` - Draw cells by holding down the mouse.

License: MIT
