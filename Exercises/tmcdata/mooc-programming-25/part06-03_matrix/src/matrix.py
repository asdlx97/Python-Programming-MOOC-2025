"""The file matrix.txt contains a matrix in the format specified in the example below:

1,0,2,8,2,1,3,2,5,2,2,2
9,2,4,5,2,4,2,4,1,10,4,2
...etc...
Please write two functions, named matrix_sum and matrix_max.
Both go through the matrix in the file, and then return the sum of
the elements or the element with the greatest value, as the names of
the functions imply.

Please also write the function row_sums, which returns a list containing
the sum of each row in the matrix. For example, calling row_sums when
the matrix in the file is defined as

1,2,3
2,3,4

the function should return the list [6, 9].

Hint: you can also include other helper functions in your program.
It is very worthwhile to spend a moment considering which functionalities
are shared by the three functions you are asked to write.
Notice that the three functions named above do not take any arguments,
but any helper functions you write may take arguments.
The file you are working with is always named matrix.txt.

NB: If Visual Studio Code can't find the file and you have checked that
there are no spelling errors, take a look at the instructions before this exercise."""


# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        matrix_sum = 0
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")

            for part in parts:
                matrix_sum += int(part)

        return matrix_sum


def matrix_max():
    with open("matrix.txt") as new_file:
        matrix_max = 0
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")

            for part in parts:
                if int(part) > matrix_max:
                    matrix_max = int(part)

        return matrix_max


def row_sums():
    with open("matrix.txt") as new_file:
        row_sums = []
        for line in new_file:
            row_sum = 0
            line = line.replace("\n", "")
            parts = line.split(",")

            for part in parts:
                row_sum += int(part)

            row_sums.append(row_sum)

        return row_sums


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())

"""
# Suggested solution

def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m
 
# Yhdistää matriisin rivit yhdeksi listaksi
def combine(matriisi: list):
    mlist = []
    for row in matriisi:
        mlist += row
    
    return mlist
 
def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)
 
def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)
 
def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums
        
# write your solution here
    
#Review
Same output, my solution didn't make use of any helper functions, I should have 
taken the time to think about these. Especially for the reading of the matrix.
 """
