"""
Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, 
from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test

"""
# Write your solution here
input_string = input("Please type in a string: ")
loop_variable = len(input_string)-1 #Minus one otherwise it excludes at first print, results in empty line

while loop_variable >= 0: #We count down so use 0 as a limit instead of len(input_string)
    print(input_string[loop_variable:]) #Suffices to put the loop variable at the start
    loop_variable -= 1 #Counting down instead of up

"""
# Suggested solution

string = input("Please type in a string: ")
 
start = len(string) - 1
while start >= 0:
    print(string[start:])
    start -= 1

#Review
Same script, same output. Was more work than expected to adapt from previous exercise, 
but lots of fun!

#TODO Rewrite this with a for loop once covered in the course
""" 