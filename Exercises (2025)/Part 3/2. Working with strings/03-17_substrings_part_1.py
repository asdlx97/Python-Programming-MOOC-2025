"""
Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test

"""
# Write your solution here
input_string = input("Please type in a string: ")
loop_variable = 1 #Indexes start at 0 to slice but if I put this on 0 then it prints an empty line? If 1 it's ok.
#After reading up on it in the course I found that they are half-open intervals, so in a:b, b isn't included in slice!!

while loop_variable <= len(input_string):
    print(input_string[:loop_variable])
    loop_variable += 1

"""
# Suggested solution

string = input("Please type in a string: ")
 
length = 1
while length <= len(string):
    print(string[0:length])
    length += 1

#Review
Was quiet intuitive but I didn't read up the course material before starting this,
which made me wonder why I first got a blank line printed when setting the loop variable to 0.

After reading up that the slicing is exclusive in the end it all made sense.

""" 