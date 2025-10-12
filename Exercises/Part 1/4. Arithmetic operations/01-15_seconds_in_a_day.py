"""
Please write a program which asks the user for a number of days. 
The program then prints out the number of seconds in the amount of days given.

The program should function as follows:

Sample output
How many days? 1
Seconds in that many days: 86400
Another example:

Sample output
How many days? 7
Seconds in that many days: 604800

"""
# Write your solution here
days = int(input("How many days? "))

print(f"Seconds in that many days: {days * 60 * 60 * 24}")

"""
#Suggested Solution

how_many = input("How many days? ")
days = int(how_many)
seconds = days * 24 * 60 * 60
print(f"Seconds in that many days: {seconds}")

#Review
The two extra variables 'days' and 'seconds' are great for clarity but not strictly necessary.
At first I forgot to convert my string input to an integer, but quickly fixed it after running it once.
"""