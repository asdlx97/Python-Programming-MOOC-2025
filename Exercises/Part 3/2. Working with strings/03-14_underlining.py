"""
Please write a program which asks the user for strings using a loop. 
The program prints out each string underlined as shown in the examples below. 
The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

Sample output
Please type in a string: Hi there!

Hi there!
---------
Please type in a string: This is a test

This is a test
--------------
Please type in a string: a

a
-
Please type in a string:

"""
# Write your solution here
input_string = "start"

while input_string != "":
    input_string = input("Please type in a string: ")
    print(f"{input_string}\n" + "-"*len(input_string))

"""
# Suggested solution

while True:
    string = input("Please type in a string: ")
    if string == "":
        break
    print(string)
    print(len(string) * "-")

#Review
My solution results in a slightly different output than expected as it still prints the 
final input line when the user just presses enter. Using the while True looping condition
is better as I don't have to define a variable in advance before the loop. 

My single f-string looks clever but a bit messy in my opinion.

#TODO add to Loop checklist
Do I need a loop condition or can I just use True?
""" 