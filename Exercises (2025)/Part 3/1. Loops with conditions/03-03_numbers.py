"""
Please write a program which asks the user for a number. 
The program then prints out all integer numbers greater than zero but smaller than the input.

Sample output
Upper limit: 5
1
2
3
4

Please don't use the value True as the condition of your while loop in this exercise!

"""
# Write your solution here
upper_limit = int(input("Upper limit: "))
number = 1

while number > 0 and number < upper_limit:
    
    print(number)
    number += 1


"""
# Suggested solution

limit = int(input("Upper limit: "))
number = 1
while number < limit:
    print(number)
    number += 1

#Review
My solution results in the same output, but is slightly over-specified comparing to the suggested one as the iteration
variable wil always be bigger than 1 and thus bigger than zero. Which makes my condition 'number' > 0 redundant.
"""