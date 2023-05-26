# Initialize the puzzle as a 2D array.

puzzle = [
    
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

# isEmpty function for finding th locations of empty cells in the puzzle.

def isEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

"""
Test for verifying that the location of empty cells are correctly located.
EMPTY = isEmpty(puzzle)
if EMPTY:
    row, col = EMPTY
    print({row}, {col})
else:
    print("No Empty Cells.")
    
"""

def puzzlePrint(original_grid, solved_grid):
    print("Original Puzzle:")
    for i, row in enumerate(original_grid):
        if i % 3 == 0:
            print("- - - - - - - - - - - - -")
        for j, num in enumerate(row):
            if j % 3 == 0:
                print("|", end=" ")
            print(num, end=" ")
            if j == 8:
                print("|", end=" ")
        print()

    print("\nSolution:")
    for i, row in enumerate(solved_grid):
        if i % 3 == 0:
            print("- - - - - - - - - - - - -")
        for j, num in enumerate(row):
            if j % 3 == 0:
                print("|", end=" ")
            print(num, end=" ")
            if j == 8:
                print("|", end=" ")
        print()

    print("- - - - - - - - - - - - -")


def isValid(grid, row, col, num):
    # Find if num exists in the same row
    for c in range(9):
        if grid[row][c] == num:
            return False
    
    # Find if num exists in the same column
    for r in range(9):
        if grid[r][col] == num:
            return False
        
    # Determine if num exists in the 3x3 grid
    sub_row = (row // 3) * 3
    sub_col = (col // 3) * 3
    
    for r in range(sub_row, sub_row + 3):
        for c in range(sub_col, sub_col + 3):
            if grid[r][c] == num:
                return False
            
    return True  # If valid

def solvingAlg(grid):
    # Find an empty cell
    empty_cell = isEmpty(grid)
    
    # Cells = Filled, Solution = Found
    if empty_cell is None:
        return True
    
    row, col = empty_cell
    
    # Obtain a possible solution from each section (1-9)
    for num in range(1, 10):
        if isValid(grid, row, col, num):
            grid[row][col] = num
            
            if solvingAlg(grid):
                return True
            
            grid[row][col] = 0
            
    return False

solvedgrid = [row[:] for row in puzzle]

if solvingAlg(puzzle):
    puzzlePrint(solvedgrid,puzzle)
else:
    print("No solution exists!")
    
     
     
        
        


            