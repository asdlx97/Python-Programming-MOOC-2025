"""
##Pre-task

Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in zero.

Sample output
Please type in integer numbers. Type in 0 to finish.
Number: 5
Number: 22
Number: 9
Number: -2
Number: 0

##Part 1: Count

After reading in the numbers the program should print out how many numbers were typed in. 
The zero at the end should not be included in the count.

You will need a new variable here to keep track of the numbers typed in.

Sample output
... the program asks for numbers
Numbers typed in 4

##Part 2: Sum

The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

The program should now print out the following:

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34

##Part 3: Mean

The program should also print out the mean of the numbers. 
The zero at the end should not be included in the calculation. 
You may assume the user will always type in at least one valid non-zero number.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5

##Part 4: Positives and negatives

The program should also print out statistics on how many of the numbers were positive and how many were negative. 
The zero at the end should not be included in the calculation.

Sample output
... the program asks for numbers
Numbers typed in 4
The sum of the numbers is 34
The mean of the numbers is 8.5
Positive numbers 3
Negative numbers 1
"""

# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.") #Pre-Task
number_amount = 0 #Part 1: Count
number_sum = 0 #Part 2: Sum
number_neg = 0
number_pos = 0

while True: #Pre-Task
    number = int(input("Number: ")) #Pre-Task

    if number == 0: #Pre-Task
        break #Pre-Task

    if number > 0: #Part 4: Positives and negatives
        number_pos += 1 #Part 4: Positives and negatives
    else: #Part 4: Positives and negatives
        number_neg += 1 #Part 4: Positives and negatives

    number_amount += 1 #Part 1: Count
    number_sum += number #Part 2: Sum

print(f"Numbers typed in {number_amount}") #Part 1: Count
print(f"The sum of the numbers is {number_sum}") #Part 2: Sum
print(f"The mean of the numbers is {number_sum / number_amount}") #Part 3: Mean
print(f"Positive numbers {number_pos}") #Part 4: Positives and negatives
print(f"Negative numbers {number_neg}") #Part 4: Positives and negatives

"""
# Suggested solution

print("Please type in integer numbers. Type in 0 to finish.")
numbers = 0
sum = 0
positives = 0
 
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    numbers += 1
    sum += number
    if number>0:
        positives += 1
 
print("Numbers typed in", numbers)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum/numbers)
print("Positive numbers", positives)
print("Negative numbers", numbers-positives)

#Review
My solution results in the same output, the suggested one is a bit more clever in using less variables,
it indeed wasn't necessary to track the amount of negatives with and additional variable.
"""