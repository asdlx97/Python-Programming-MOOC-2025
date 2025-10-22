"""
The program below has some syntactic issues:

print("Are you ready?")
number = int(input("Please type in a number: "))
while number = 0:
print(number)
print("Now!")
Please fix it so that it prints out the following:

Sample output
Are you ready?
Please type in a number: 5
5
4
3
2
1
Now!

This exercise is similar to the countdown exercise in the last section, 
but please don't use a while True loop this time round!
"""
# Fix the program
print("Are you ready?")
number = int(input("Please type in a number: "))

#while number != 0: #Added exclamation mark, but this would lead to infite loops
while number > 0: #Loops only for positive integers
    print(number) #Added indentation
    number -= 1 #Added substraction of iteration variable

print("Now!")

"""
# Suggested solution

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
  print(number)
  number -= 1
print("Now!")

#Review
My solution results in the same output, but the suggested one is more efficiënt (less iterations) and cleaner (no if-statement).
Overall more elegant to do it the suggested way.
"""


