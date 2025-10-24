"""
Please write a new version of the program in the previous exercise. 
In addition to the result it should also print out the calculation performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Sample output
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

You may assume the number typed in by the user is always equal to 2 or higher.


"""
# Write your solution here
limit = int(input("Limit: "))
counter = 1
sum = 0
consecutive_sum = "1" #Added empty string

while sum < limit:
    sum += counter
    if counter > 1:
        consecutive_sum += f" + {counter}" #Updates initialized string
    counter += 1
    
print(f"The consecutive sum: {consecutive_sum} = {sum}")

"""
# Suggested solution

limit = int(input("Limit: "))
number = 1
sum = 1
numbers = "1"
while sum < limit:
    number += 1
    sum += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {sum}")

#Review
My solution results in the same output, suggested one manually starts the sum at 1, which I think
is a bit less intuitive as I rather let the loop looping.
"""  