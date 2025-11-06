"""
Please write a function named square, which prints out a square of characters, and takes two arguments. 
The first parameter specifies the length of the side of the square. 
The second parameter specifies the character used to draw the square.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

square(5, "*")
print()
square(3, "o")

Sample output
*****
*****
*****
*****
*****

ooo
ooo
ooo
"""

# Copy here code of line function from previous exercise
def line (length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

def square(size, character):
    # You should call function line here with proper parameters
    i = size
    while i > 0:
        line(size, character)
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")

"""
# Suggested Solution

def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
 
def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1

#Review
My suggestion results in the same output. Suggested one just uses another loop variable.
"""