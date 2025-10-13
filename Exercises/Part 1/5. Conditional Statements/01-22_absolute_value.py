"""
Please write a program which asks the user for an integer number. 
If the number is less than zero, the program should print out the number multiplied by -1. 
Otherwise the program prints out the number as is. Please have a look at the examples of expected behaviour below.

Sample output
Please type in a number: -7
The absolute value of this number is 7

Sample output
Please type in a number: 1
The absolute value of this number is 1

Sample output
Please type in a number: -99
The absolute value of this number is 99

"""
# Write your solution here
number = int(input("Please type in a number: "))

if number < 0:
    print(f"The absolute value of this number is {number * -1}")

if number >= 0:
    print(f"The absolute value of this number is {number}")

"""
#Suggested Solution

number = int(input("Please type in a number: "))
absolute_value = number
if number < 0:
    absolute_value = number * -1
print("The absolute value of this number is", absolute_value)
 
#Review
My solution results in the same output. The suggested one uses a single conditional statement which is more efficient 
but requires the use of an additional variable. An if-else statement could also be used here but we haven't seen that one yet in the course. 

"""