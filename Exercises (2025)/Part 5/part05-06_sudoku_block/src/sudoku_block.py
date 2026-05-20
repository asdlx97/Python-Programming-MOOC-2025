"""
Please write a function named block_correct(sudoku: list, row_no: int,
column_no: int), which takes a two-dimensional array representing a
sudoku grid, and two integers referring to the row and column indexes of
a single square, as its arguments. Rows and columns are indexed from 0.

The function should return True or False depending on whether the 3 by 3
block to the right and down from the given indexes is filled in correctly.
That is, whether the block contains each of the numbers 1 to 9 at most once.

Notice that this function does not strictly follow the rules of sudoku.
In a real game of sudoku there are only 9 blocks to check, and these are
located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3)
and (6, 6). Such restrictions on indexes should not be implemented here.

sudoku = [
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

print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))

Sample output
False
True
The first function call should check the 3 by 3 block beginning with
the square at indexes 0, 0:

9 0 0
2 0 0
0 2 0

The second function call should check the 3 by 3 block beginning with
the square at row 1, column 2:

0 2 5
0 3 0
4 0 0
This second block would not be checked in an actual game of sudoku,
but your function should allow for it to be checked.
"""


# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    block_check = []

    for row in sudoku[row_no : row_no + 3]:
        for cell in row[column_no : column_no + 3]:
            if cell != 0 and cell in block_check:
                return False
            block_check.append(cell)
        # return True here didn't work, as it was too early to return
    return True


if __name__ == "__main__":
    sudoku = [
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))

"""
# Suggested Solution

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True

#Review
My solution results in the same output, the assigned one used one more
variable inbetween by assigning the matric cell or element to it using their
coordinates, which I agree is good practise as I haven't used that before. 
"""
