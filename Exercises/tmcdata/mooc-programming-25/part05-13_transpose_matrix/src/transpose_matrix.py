"""
Please write a function named transpose(matrix: list),
which takes a two-dimensional integer array, i.e., a matrix,
as its argument. The function should transpose the matrix.

Transposing means essentially flipping the matrix over its diagonal:
columns become rows, and rows become columns.

You may assume the matrix is a square matrix,
so it will have an equal number of rows and columns.

The following matrix

1 2 3
4 5 6
7 8 9
transposed looks like this:

1 4 7
2 5 8
3 6 9

The function should not have a return value.
The matrix should be modified directly through the reference.
"""


# Write your solution here
def transpose(matrix: list):
    length = len(matrix)

    # Make a true copy of matrix by making an empty one
    original_matrix = []

    # Copy the amount of rows into the new matrix
    for rows in range(length):
        original_matrix.append([])

    # Append every cell of matrix in the new matrix
    for row in range(0, length):
        for column in range(0, length):
            original_matrix[row].append(matrix[row][column])

    # Replace all values in matrix row/column by column/row value from copied matrix
    for r in range(0, length):
        for c in range(0, length):
            matrix[r][c] = original_matrix[c][r]


if __name__ == "__main__":
    my_matrix = [[1, 2], [1, 2]]
    print(transpose(my_matrix))

"""
# Suggested Solution

def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
 
            #..or alternatively
            # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#Review
My solution returns the same output, but the suggested one is structurally 
more efficient. Instead of creating a full copy of the matrix, it swaps 
elements in place across the diagonal, minimizing both memory use and complexity. 
The nested loop in the suggested version also cleverly starts from j = i, ensuring 
each pair is swapped only once.
"""
