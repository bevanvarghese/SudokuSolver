# Sudoku Solver
A GUI-based Sudoku Solver that visualizes constraint-satisfaction using the backtracking algorithm.

### Constraints
1. Each cell must contain a number from 1 to 9.
2. Each row must contain every number from 1 to 9 (each appearing once).
3. Each column must contain every number from 1 to 9 (each appearing once).
4. The grid contains nine 3x3 boxes. Each such box must contain every number from 1 to 9 (each appearing once).

### How to use?
* For a visualization of the algorithm, run SudokuSolverGUI.py. Press Space to solve.  _Note: This requires the PyGame module installed._
* For a text-based solver, run SudokuSolver.py.
* To enter your own game-board, change the "board" variable in the respective file, using 0 to indicate empty cells.  
  SudokuSolverGUI.py: lines 21-29   
  SudokuSolver.py: lines 1-9

### Demo

![withoutdelay](https://user-images.githubusercontent.com/48976616/86795702-74c0c900-c08b-11ea-9bc0-7ff7f4c71295.gif)

To slow down the visualizer, remove the # from lines 69 and 78. Insert the "delay" time you want between frames within the brackets (in milliseconds). 
For example, if you want a delay of 5 milliseconds between each frame, lines 69 and 78 would look like this:
`pygame.time.delay(5)`

### Future development
I plan on scaling this to a fully-functional game with time. 
