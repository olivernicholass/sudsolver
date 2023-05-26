# Sudoku Solver using Recursive Backtracking

The Definition of a 9x9 Matrix where 0 represents an empty cell.

$$X \in \mathbb{Z}_{0+}^{9 * 9}$$

$$X=\left[\begin{array}{ccccc}
x_{11} & x_{12} & x_{13} & \ldots & x_{19} \\
x_{21} & x_{22} & x_{23} & \ldots & x_{29} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
x_{91} & x_{92} & x_{93} & \ldots & x_{99}
\end{array}\right]$$

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
