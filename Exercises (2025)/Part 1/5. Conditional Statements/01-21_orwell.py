"""
Please write a program which asks the user for an integer number. 
The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

Sample output
Please type in a number: 2020

Sample output
Please type in a number: 1984
Orwell

"""
# Write your solution here
number = int(input("Please type in a number: "))

#Start conditional statement
if number == 1984: #Conditional Expression
    print("Orwell") #(Conditional) Block
#End conditional statement

"""
#Suggested Solution

number = int(input("Please type in a number: "))
if number == 1984:
    print('Orwell')
 
#Review
My solution results in the same output. The suggested one uses single quotes for the string print function, 
I checked again why that would be useful and it's when you'd use special characters or double quotes within
the string value to avoid escaping quotes. 

At first I also forgot to use the colon at the end of my conditional expression, which I fixed after getting an error in the terminal
"""