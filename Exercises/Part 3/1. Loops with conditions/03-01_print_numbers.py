"""
Please write a program which prints out all the even numbers between two and thirty, using a loop. 
Print each number on a separate line.

The beginning of your output should look like this:

Sample output

2
4
6
8
etc...

"""
# Write your solution here
number = 2 #Starts at two

while number <= 30:
    if number % 2 == 0:
        print(number)
    
    number += 1

"""
# Suggested solution

number = 2
while number <= 30:
    print(number)
    number += 2

#Review
My solution results in the same output, but the suggested one is more efficiënt (less iterations) and cleaner (no if-statement).
Overall more elegant to do it the suggested way.
"""