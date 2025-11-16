"""
Please write a function named row_correct(sudoku: list, row_no: int),
which takes a two-dimensional array representing a sudoku grid, and
an integer referring to a single row, as its arguments. Rows are indexed from 0.

The function should return True or False, depending on whether the
row is filled in correctly, that is, whether it contains each of
the numbers 1 to 9 at most once.

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

print(row_correct(sudoku, 0))
print(row_correct(sudoku, 1))

Sample output
True
False
"""


# Write your solution here
def row_correct(sudoku: list, row_no: int):

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

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))

"""
# Suggested Solution

def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True

#Review
My two solutions returns the same output, the suggested one immediately returns false
to break the for loop before appending, which may be a bit more efficiënt.
"""
