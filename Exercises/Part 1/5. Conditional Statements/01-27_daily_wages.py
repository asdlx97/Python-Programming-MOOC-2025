"""
Please write a program which asks for the hourly wage, hours worked, and the day of the week. 
The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, 
except on Sundays when the hourly wage is doubled.

Sample output
Hourly wage: 8.5
Hours worked: 3
Day of the week: Monday
Daily wages: 25.5 euros

Sample output
Hourly wage: 12.5
Hours worked: 10
Day of the week: Sunday
Daily wages: 250.0 euros

"""
# Write your solution here
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
isSunday = False

if day == "Sunday" or day == "sunday":
    isSunday = True

if isSunday:
    print(f"Daily wages: {wage * hours * 2} euros")

else:
    print(f"Daily wages: {wage * hours} euros")

"""
#Suggested Solution

hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
weekday = input("Day of the week: ")
 
if weekday == "Sunday":
    # The salary is double on Sundays
    hourly_wage *= 2
 
total_wage = hourly_wage * hours_worked
print(f"Daily wages: {total_wage} euros")

#Review
My solution results in the same output. The suggested one is a bit more concise as it uses
one less variable and converts the hourly wage on sunday immediately, which may be easier to adjust if the
sunday wage calculation ever changes.

I tried to take into account that people might input a small caps sunday, but I'm sure there are
better ways to handle those cases with default functions that we probably see later on in the course.
I could also have taken into account error handeling when people are inputting days that don't exist.
"""