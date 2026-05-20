"""
Please write a program which asks the user for a year, and prints out the next leap year.

Sample output
Year: 2023
The next leap year after 2023 is 2024
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

Sample output
Year: 2024
The next leap year after 2024 is 2028

"""
# Write your solution here
year = int(input("Year: "))
next_year = year + 1
leap_year = False
next_leap_year = 0
 
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True

while True:
    if next_year % 100 == 0:
        if next_year % 400 == 0:
            next_leap_year = next_year
            break
    elif next_year % 4 == 0:
        next_leap_year = next_year
        break
    
    next_year += 1

print(f"The next leap year after {year} is {next_leap_year}")

"""
# Suggested solution

start_year = int(input("Year: "))
year = start_year + 1
while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
 
    year += 1
 
print(f"The next leap year after {start_year} is {year}")
 

#Review
My solution results in the same output, but the suggested one doesn't check if the given start year is a leap year itself,
it goes straight to calculating if the year after is a leap one. Which is fine because we don't need to know if 
the given year is a leap year. 

The suggested one is thus more concise, but mine is more maintainable in the future for when we 
want to do something with that boolean. 
"""

