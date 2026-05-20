"""
Please write a program which asks the user to choose between addition and removal. 
Depending on the choice, the program adds an item to or removes an item from the end of a list. 
The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.

The list is printed out in the beginning and after each operation. 
Have a look at the example execution below:

Sample output
The list is now []
a(d)d, (r)emove or e(x)it: d
The list is now [1]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: r
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: x
Bye!
You may assume that, if the list is empty, there will not be an attempt to remove items.

NB: this exercise doesn't ask you to write any functions, 
so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
list = []

while True:
    print(f"The list is now {list}")
    answer = input("a(d)d, (r)emove or e(x)it: ")

    if answer == "x":
        break
    elif answer == "d":
        if len(list) == 0:
            list.append(1)
        else:
            list.append(list[-1]+1)
    elif answer == "r":
        list.pop(-1)

print("Bye!")

"""
# Suggested Solution

list = []
while True:
    print(f"The list is now {list}")
    selection = input("a(d)d, (r)emove or e(x)it:")
    if selection == "d":
        # Value of item is length of the list + 1
        item = len(list) + 1
        list.append(item)
    elif selection == "r":
        list.pop(len(list) - 1)
    elif selection == "x":
        break
 
print("Bye!")

#Review
My suggestion results in the same output. Suggested one literally uses the length of
the list to calculate nex number in line, which works as these are increments of 1 in this case.
This means it also doesn't need to check if list is empty or not to decide to start with 1.

I however used list[-1] to access last item which is more pythonic?

I shouldn't use the name 'list' to asign my list to tho, could get me in trouble later on.
"""