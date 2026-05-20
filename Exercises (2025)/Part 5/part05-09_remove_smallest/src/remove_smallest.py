"""
Please write a function named remove_smallest(numbers: list),
which takes a list of integers as its argument.

The functions should find and remove the smallest item in the list.
You may assume there is a single smallest item in the list.

The function should not have a return value - it should directly modify
the list it receives as a parameter.

An example of how the function works:

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
Sample output
[2, 4, 6, 3, 5]
"""


# Write your solution here
def remove_smallest(numbers: list):
    smallest_number = sorted(numbers)[
        0
    ]  # Don't use the .sort() method as that changes the original list which I don't know if its allowed here

    numbers.remove(smallest_number)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)

"""
# Suggested Solution

def remove_smallest(numbers: list):
    smallest = min(numbers)
    numbers.remove(smallest)

#Review
My solution gives the same output. The suggested one is a bit more clever
and concise by using the min() function. 