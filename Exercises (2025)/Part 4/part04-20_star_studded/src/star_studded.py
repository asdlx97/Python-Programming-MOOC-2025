"""
Please write a program which asks the user to type in a string. 
The program then prints each input character on a separate line. 
After each character there should be a star (*) printed on its own line.

This is how it should work:

Sample output
Please type in a string: Python
P
*
y
*
t
*
h
*
o
*
n
*

NB: this exercise doesn't ask you to write any functions, 
so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
input_string = input("Please type in a string: ")

for letter in input_string:
    print(letter)
    print("*")

"""
# Suggested Solution

string = input("Anna merkkijono: ")
for char in string:
    print(char)
    print("*")

#Review
Same script, same output. 
"""