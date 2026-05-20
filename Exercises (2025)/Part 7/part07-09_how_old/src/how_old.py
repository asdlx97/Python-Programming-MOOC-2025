"""
Please write a program which asks the user for their date of birth,
and then prints out how old the user was on the eve of the new millennium.
The program should ask for the day, month and year separately, and print
out the age in days. Please have a look at the examples below:

Sample output
Day: 10
Month: 9
Year: 1979
You were 7417 days old on the eve of the new millennium.

Sample output
Day: 28
Month: 3
Year: 2005
You weren't born yet on the eve of the new millennium.

You may assume all day-month-year combinations given as an argument will
be valid dates. That is, there will not be a date like February 31st.
"""

# Write your solution here
from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthday = datetime(year, month, day)

eve_millenium = datetime(1999, 12, 31)

difference = eve_millenium - birthday

if birthday > eve_millenium:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {difference.days} days old on the eve of the new millennium.")

"""
# Suggested solution

from datetime import datetime
 
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
 
time = datetime(year, month, day)
millenium = datetime(1999, 12, 31)
 
if time > millenium:
    print ("You weren't born yet on the eve of the new millennium.")
else:
    ika = millenium - time
    print (f"You were {ika.days} days old on the eve of the new millennium.")

#Review
Same output, nearly same script.
"""
