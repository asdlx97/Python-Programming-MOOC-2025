"""
This is the very last sudoku task. This time we will create a slightly different
version of the function for adding new numbers to the grid.

The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int)
takes a two-dimensional array representing a sudoku grid, two integers referring
to the row and column indexes of a single square, and a single digit between 1 and 9,
 as its arguments. The function should return a copy of the original grid with the
 new digit added in the correct location.

 The function should not change the original grid received as a parameter.

The print_sudoku function from the previous exercise could be useful for testing,
and it is used in the example below:

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

grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)

Sample output
Original:
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Copy:
2 _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Hint When dealing with nested lists you should be extra careful when copying.
What all needs to be explicitly copied, and where do changes actually have an effect?

The visualisation tool is a great help here, too, although the size of the sudoku
grid will make the view less orderly than usual.
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


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_sudoku = []

    for row in sudoku:
        copy_sudoku.append(row[:])

    copy_sudoku[row_no][column_no] = number

    return copy_sudoku


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

"""
# Suggested Solution

def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
 
    new_list[row_no][column_no] = number
    return new_list

#Review
My solution produces the same output. Structurally, it’s almost identical to 
the suggested one — both correctly create a deep copy of the sudoku grid by 
slicing each row before modifying it. The only difference is naming: 
the suggested version uses clearer, shorter variable names (new_list and r), 
which improves readability slightly. 
Functionally, the logic and handling of nested lists are the same 
"""
