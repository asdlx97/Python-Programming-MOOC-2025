"""
Please write a program which asks the user to type in a number. 
The program then prints out all the positive integer values from 1 up to the number. 
However, the order of the numbers is changed so that each pair or numbers is flipped. 
That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

Sample output
Please type in a number: 5
2
1
4
3
5

Sample output
Please type in a number: 6
2
1
4
3
6
5
"""
# Write your solution here
number = int(input("Please type in a number: "))
i = 1

while i <= number:
    if i+1 <= number:
        print(i+1)
    

    if i <= number:
        i += 1
        print(i-1)
        i += 1

"""
# Suggested solution

number = int(input("Please type in a number: "))
 
index = 1
while index+1 <= number:
    print(index+1)
    print(index)
    index += 2
 
if index <= number:
    print(index)

#Review
My solution results in the same output but is less clean than suggested one. 
Not good to nest too much if statements in conditional ones. 

#TODO Maybe try to do this again using a for loop
""" 
