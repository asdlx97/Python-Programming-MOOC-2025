"""
Please write a function named shape, which takes four arguments. 
The first two parameters specify a triangle, as above, and the character used to draw it. 
The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. 
The fourth parameter specifies the filler character of the rectangle. 
The function prints first the triangle, and then the rectangle below it.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")

Sample output
X
XX
XXX
XXXX
XXXXX
*****
*****
*****

o
oo
++
++
++
++

.
..
...
Hint

Don't try and solve this exercise "all at once". 
A good first step would be to make sure you can print the triangle reliably. 
Then you can try adding the rectangle.

This is one of the most important skills of a programmer: concentrate on small, tangible sections of the problem at a time. 
Solve and verify partial solutions, and use them to build towards a complete solution.
"""

# Copy here code of line function from previous exercise and use it in your solution
def line (length, string):
    if string == "":
        print("*" * length)
    else:
        print(string[0] * length)

def shape (size_width, triangle_character, height, rectangle_character):
    i = 1
    j = height

    while i <= size_width:
        line(i, triangle_character)
        i += 1
    
    while j > 0:
        line(size_width, rectangle_character)
        j -= 1

    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")


"""
# Suggested Solution

def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
 
def shape(y_height, y_character, a_height, a_character):
    i = 1
    while i <= y_height:
        line(i, y_character)
        i += 1
    i = a_height
    while i > 0:
        line(y_height, a_character)
        i -= 1

#Review
My suggestion results in the same output. Suggested one uses the same loop variable and repurposes it after 
the first while loop, which is kind of smart. 
"""