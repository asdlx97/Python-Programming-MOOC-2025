"""
Please write a program which asks for the user's name. 
If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. 
The price of a single portion is 5.90.

Two examples of the program's execution:

Sample output
Please tell me your name: Kramer
How many portions of soup? 2
The total cost is 11.8
Next please!

Sample output
Please tell me your name: Jerry
Next please!

"""
# Write your solution here
name = input("Please tell me your name: ")

if name != "Jerry":
    amountOfPortions = int(input("How many portions of soup? "))
    print(f"The total cost is {amountOfPortions * 5.9}")

print("Next please!")

"""
#Suggested Solution

name = input("Please tell me your name:  ")
if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    cost = 5.9 * portions
    print("The total cost is", cost)
print("Next please!")
 
#Review
The suggested solution has more simple variable names, it looks a bit cleaner.
It also uses an extra variable for cost calculation, this does seem to make the code cleaner and I'll try to do that more often in the future.

My solution uses f-strings instead of comma separated printing. The latter is older, tha's why I use the preferred new f-string print.
"""