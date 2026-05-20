"""
Please write a function named triangle, which draws a triangle of hashes, and takes one argument. 
The triangle should be as tall and as wide as the value of the argument.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

triangle(6)
print()
triangle(3)

Sample output
#
##
###
####
#####
######

#
##
###
"""

# Copy here code of line function from previous exercise
def line (length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

def triangle(size):
    # You should call function line here with proper parameters
    triangle_length = 1
    i = size

    while i > 0:
        line(triangle_length, "#")
        i -= 1
        triangle_length += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

"""
# Suggested Solution

def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
 
def triangle(size):
    i = 0
    while i < size:
        i += 1
        line(i, '#')

#Review
My suggestion results in the same output. Suggested one uses only one variable and the same variable for bith the loop variable 
and the size argument for the line function, which makes totally sense and is more efficiënt. 
"""