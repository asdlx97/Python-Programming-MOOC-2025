"""
Please write a function named chessboard, which prints out a chessboard made out of 
ones and zeroes. The function takes an integer argument, which specifies the length of 
the side of the board. 

See the examples below for details:

chessboard(3)
print()
chessboard(6)

Sample output
101
010
101

101010
010101
101010
010101
101010
010101
"""
# Write your solution here
def chessboard(size):
    number = size

    while number > 0:
        print(("10"*size)[:size])
        number -= 1
        if number > 0:
            print(("01"*size)[:size])
            number -= 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)

"""
# Suggested solution

def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

#Review
My solution results in the same output. The suggested one is more math based, and
decides line by line where mine thinks in pairs. 
""" 