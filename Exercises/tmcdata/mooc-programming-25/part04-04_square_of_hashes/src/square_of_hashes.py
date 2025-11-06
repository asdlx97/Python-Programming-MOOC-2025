"""
Please write a function named box_of_hashes, 
which prints out a rectangle of hash characters. 
The function takes one argument, which specifies the height of the rectangle. 
The rectangle should be ten characters wide.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. 
Please don't change anything in your line function.

Some examples of how the function should work:

box_of_hashes(5)
print()
box_of_hashes(2)
"""

# Copy here code of line function from previous exercise
def line (length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    height = size

    while height > 0:
        line(size, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

"""
# Suggested Solution

def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
 
def square_of_hashes(size):
    i = 0
    while i < size:
        line(size, "#")
        i += 1

#Review
My suggestion results in the same output. Suggested one just uses another loop variable.
"""