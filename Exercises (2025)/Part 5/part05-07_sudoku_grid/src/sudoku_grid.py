"""
Please write a function named sudoku_grid_correct(sudoku: list),
which takes a two-dimensional array representing a sudoku grid as its argument.
The function should use the functions from the three previous exercises to determine
whether the complete sudoku grid is filled in correctly. Copy the functions from
the exercises above into your Python code file for this exercise.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid.
If all contain each of the numbers 1 to 9 at most once, the function returns True.
If a single one is filled in incorrectly, the function returns False.

The image of a sudoku grid above these exercises has the nine blocks within the grid
indicated with thicker borders. These are the blocks the function should check,
and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))

Sample output
False
True
"""


# Write your solution here
def row_correct(sudoku: list, row_no: int):
    # return True  # Debug statement
    row_check = []
    for square in sudoku[row_no]:
        # if square == 0 or square not in row_check:
        #     row_check.append(square)
        # else:
        #     return False
        if square not in row_check:
            if square != 0:
                row_check.append(square)
        else:
            return False

    return True


def column_correct(sudoku: list, column_no: int):
    column_check = []

    for row in sudoku:
        square = row[column_no]
        if square > 0 and square in column_check:
            return False
        column_check.append(square)

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    block_check = []

    for row in sudoku[row_no : row_no + 3]:
        for cell in row[column_no : column_no + 3]:
            if cell != 0 and cell in block_check:
                return False
            block_check.append(cell)
        # return True here didn't work, as it was too early to return
    return True


def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        rows_correct = row_correct(sudoku, i)
        if not rows_correct:
            return False  # Forgot this at first, so kept going even the second row was False. Found during debugging.

    if rows_correct:
        for j in range(9):
            columns_correct = column_correct(sudoku, j)
            if not columns_correct:
                return False  # Forgot this at first, so kept going even if a column was False. Found during debugging.

    if rows_correct and columns_correct:
        for k in range(0, 9, 3):
            for l in range(0, 9, 3):
                blocks_correct = block_correct(sudoku, k, l)
                if not blocks_correct:
                    return False

    return True


if __name__ == "__main__":
    sudoku = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 6, 0, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]
    print(sudoku_grid_correct(sudoku))

    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(sudoku_grid_correct(sudoku2))

"""
# Suggested Solution

def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True
 
def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
 
    return True

#Review
My solution results in the same output. The suggested one is structurally simpler, 
as it removes the extra conditional checks and nested variables I used. 
Instead of tracking separate flags like rows_correct or columns_correct, 
it returns immediately when an error is found. This makes the code more 
concise and easier to maintain, something I’ll aim for next time. 
"""
