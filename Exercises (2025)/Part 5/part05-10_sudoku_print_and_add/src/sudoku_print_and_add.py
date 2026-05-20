"""
In this exercise we will complete two more functions for the sudoku project
from the previous section: print_sudoku and add_number.

The function print_sudoku(sudoku: list) takes a two-dimensional array representing
a sudoku grid as its argument. The function should print out the grid in the
format specified in the examples below.

The function add_number(sudoku: list, row_no: int, column_no: int, number:int)
takes a two-dimensional array representing a sudoku grid,
two integers referring to the row and column indexes of a single square,
and a single digit between 1 and 9, as its arguments.

The function should add the digit to the specified location in the grid.

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)

Sample output
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Three numbers added:

2 _ _  _ _ _  _ _ _
_ _ 7  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ 3 _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Hint

Remember it is possible to call the print function without causing a line change:

print("characters ", end="")
print("without carriage returns", end="")

Sample output
characters without carriage returns

Sometimes you need just a new line, which a print statement without any
argument will achieve:

print()
"""


# Write your solution here
def print_sudoku(sudoku: list):
    i = 0
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku[row][column] != 0:
                print(str(sudoku[row][column]) + " ", end="")
            elif column != 8:
                print("_ ", end="")
            else:
                print("_", end="")

            if (column + 1) % 3 == 0 and column < 7:
                print(" ", end="")

            if column == 8:
                print()

        if (row + 1) % 3 == 0:
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)

"""
# Suggested Solution

def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()
 
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

#Review
My solution produces the same output. Structurally, the suggested one is more 
compact and emphasizes readability by iterating directly over rows and cells 
instead of using index ranges. It separates spacing and formatting logic more 
clearly by building a small string m for each cell before printing, 
which keeps the print logic neat and reduces conditional clutter. 
"""
