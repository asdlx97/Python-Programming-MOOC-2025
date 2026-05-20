"""
Generally, any year that is divisible by four is a leap year. 
However, if the year is additionally divisible by 100, 
it is a leap year only if it also divisible by 400.

Please write a program which asks the user for a year, 
and then prints out whether that year is a leap year or not.

Some examples:

Sample output
Please type in a year: 2011
That year is not a leap year.

Sample output
Please type in a year: 2020
That year is a leap year.

Sample output
Please type in a year: 1800
That year is not a leap year.

"""
#Write your solution here

year = int(input("Please type in a year: "))

if year % 4 == 0 and year % 100 == 0: 
    if year % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

"""
# Suggested solution
year = int(input("Please type in a year: "))
 
# First, we make assumption that a year is not a leap year
leap_year = False
 
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True
 
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
 

#Review
My solution results in same output, but the suggested one is using Booleans 
to make the print statement in the end, which is cleaner and I'll try to do
that in the future.

Suggested solution also uses slightly reordered logic that's not as 
intuitive when reading the stated problem at first, but makes absolute mathematical sense. 
"""
