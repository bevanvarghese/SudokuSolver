# Sudoku Solver
A GUI-based Sudoku Solver that visualizes constraint-satisfaction using the backtracking algorithm.

### Constraints
1. Each cell must contain a number from 1 to 9.
2. Each row must contain every number from 1 to 9 (each appearing once).
3. Each column must contain every number from 1 to 9 (each appearing once).
4. The grid contains nine 3x3 boxes. Each such box must contain every number from 1 to 9 (each appearing once).

### How to use?
* For a visualization of the algorithm, run SudokuSolverGUI.py. Note that this requires the PyGame module installed.
* For a text-based solver, run SudokuSolver.py.
* To enter your own game-board, change the "board" variable in the respective file, using 0 to indicate empty cells.  
  SudokuSolverGUI.py: lines 21-29   
  SudokuSolver.py: lines 1-9

### Future development
I plan on scaling this to a fully-functional game with time. 
