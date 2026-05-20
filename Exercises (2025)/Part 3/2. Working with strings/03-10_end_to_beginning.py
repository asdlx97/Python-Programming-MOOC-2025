"""
Please write a program which asks the user for a string. 
The program then prints out the input string in reversed order, from end to beginning. 
Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h

"""
# Write your solution here
input_string = input("Please type in a string: ")
counter = len(input_string)

while counter > 0:
    print(input_string[counter-1])
    counter -= 1

"""
# Suggested solution

input_string = input("Please type in a string: ")
index = -1
while index >= -len(input_string):
    print(input_string[index])
    index -= 1

#Review
My solution results in the same output, the suggested one uses negative indexing which makes the code
a bit sleeker as you don't have to 'manually' calculate len(sequence) - 1.
""" 