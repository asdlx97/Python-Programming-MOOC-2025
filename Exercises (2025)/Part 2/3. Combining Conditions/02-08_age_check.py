"""
Please write a program which asks for the user's age. 
If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, 
the program should print out a comment.

Have a look at the examples of expected behaviour below to figure out which comment is applicable in each case.

Sample output
What is your age? 13
Ok, you're 13 years old

Sample output
What is your age? 2
I suspect you can't write quite yet...

Sample output
What is your age? -4
That must be a mistake

"""
# Write your solution here
age = int(input("What is your age? "))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif age >= 0: #and age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

"""
# Suggested solution
age = int(input("What is your age? "))
if age < 0:
    print("That must be a mistake")
elif age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("Ok, you're " + str(age) + " years old")

#Review
My solution results in the same output. Suggested solution uses the conditional
statements a bit more natural going from most unlikely to most likely default case.
Also, I included an and logical operator but this wasn't necessary as it got ruled our by first
if statement. 
"""