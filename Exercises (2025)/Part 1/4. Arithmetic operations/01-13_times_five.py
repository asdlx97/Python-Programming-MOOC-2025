"""
Please write a program which asks the user for a number. The program then prints out the number multiplied by five.

The program should function as follows:

Sample output
Please type in a number: 3
3 times 5 is 15
1

"""
# Write your solution here
number = int(input("Please type in a number: "))
print(f"{number} times 5 is {number * 5}")

"""
#Suggested solution

number = input("Please type in a number: ")
result = int(number) * 5
print(f"{number} times 5 is {result}")

#Review
Happy I was able to do it in two! lines insr-tead of just one. 
The intermediated suggested variable of 'result' was overkill as 
there are no extra operations for which this might be used, 
otherwise could be useful
"""