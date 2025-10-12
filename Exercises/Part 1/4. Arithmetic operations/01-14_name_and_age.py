"""
#Exercise 

Name and age

Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:

Sample output
What is your name? Frances Fictitious
Which year were you born? 1990
Hi Frances Fictitious, you will be 31 years old at the end of the year 2021

"""
# Write your solution here
name = input("What is your name? ")
birthYear = int(input("Which year were you born? "))

print(f"Hi {name}, you will be {2021 - birthYear} years old at the end of the year 2021")

"""
#Suggested solution

name = input("What is your name? ")
born = int(input("Which year were you born? "))
age = 2021 - born

print(f"Hi {name}, you will be {age} years old at the end of the year 2021")

#Review
Again I think the intermediate 'age' variable wasn't necessary but it makes for a cleaner print command I agree.
"""