"""
Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

The program should function as follows:

Sample output
Number 1: 3
Number 2: 7
The sum of the numbers: 10
The product of the numbers: 21

"""
# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

print(f"The sum of the numbers: {number1 + number2}")
print(f"The product of the numbers: {number1 * number2}")

"""
#Suggested Solution

number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
print("The sum of the numbers:", number1 + number2)
print("The product of the numbers:", number1 * number2)
 
 
#Review
My solution results in the same output. The only difference is that I used an f-string fot the print.

"""