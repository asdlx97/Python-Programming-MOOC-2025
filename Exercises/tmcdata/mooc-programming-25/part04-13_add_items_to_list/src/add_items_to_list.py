"""
Please write a program which first asks the user for the number of items to be added. 
Then the program should ask for the given number of values, one by one, 
and add them to a list in the order they were typed in. Finally, the list is printed out.

An example of expected behaviour:

Sample output
How many items: 3
Item 1: 10
Item 2: 250
Item 3: 34
[10, 250, 34]

NB: this exercise doesn't ask you to write any functions, 
so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
list = []

amount = int(input("How many items: "))

i = 1

while i <= amount:
    new_item = int(input(f"Item {i}: "))
    list.append(new_item)
    i += 1

print(list)

"""
# Suggested Solution

numbers = int(input("How many items: "))
list = []
 
while len(list) < numbers:
    number = int(input(f"Item {len(list) + 1}: "))
    list.append(number)
 
print(list)

#Review
My suggestion results in the same output. Suggested one doesn't uses length of list
as the loop counter, which I tought about doing but somehow opted against it, don't know why anymore..
But it crossed my mind!
"""