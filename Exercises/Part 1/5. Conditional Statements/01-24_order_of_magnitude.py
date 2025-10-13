"""
Please write a program which asks the user for an integer number. 
The program should then print out the magnitude of the number according to the following examples.

Sample output
Please type in a number: 950
This number is smaller than 1000
Thank you!

Sample output
Please type in a number: 59
This number is smaller than 1000
This number is smaller than 100
Thank you!

Sample output
Please type in a number: 2
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10
Thank you!

Sample output
Please type in a number: 1123
Thank you!

"""
# Write your solution here
number = int(input("Please type in a number: "))

if number < 1000:
    print("This number is smaller than 1000")
    if number < 100:
        print("This number is smaller than 100")
        if number < 10:
            print("This number is smaller than 10")

print("Thank you!")

"""
#Suggested Solution

number = int(input("Please type in a number: "))
if number < 1000:
    print("This number is smaller than 1000")
 
if number < 100:
    print("This number is smaller than 100")
 
if number < 10:
    print("This number is smaller than 10")
 
print("Thank you!")

#Review
The suggested solution uses independent conditional statements, where I use nested statements. 
My number only gets checked if the previous consitional expression is true, which is risky but 
the hierarchic structure isn't fatal in this case as it follows mathematical logic. 

The suggested style is preferred if you want a flat structure and make sure that all checks are passed.
"""