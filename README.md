# Sudoku Solver using Recursive Backtracking

Backtracking Algorithm Steps taken:

1.  First we use the isEmpty method to locate an empty cell in the grid
2.  Conditional statement to see if all cells are filled, if they are, then a solution was found.
3.  for num in range(1,10):
  - If an empty cell (row, col) can be filled with num, then fill it for verification.
  - If the algorithm is TRUE then we also return TRUE.
  - If the empty cell cannot be filled, then we continue to leave it as 0 to continue the backtracking process.
4. If nothing in the range can fill empty cells then there is no solution, hence we return FALSE.

Time Complexity (Worst Case): $O\left(9^m\right)$

There are other ways to approach this problem such as Rule-Based, Constraint, Crooks Algorithm and more.

Note: The print method is over-the-top but I needed it to be neat..
