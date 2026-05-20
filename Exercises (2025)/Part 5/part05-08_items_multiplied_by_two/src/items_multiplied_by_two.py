"""Please write a function named double_items(numbers: list),
which takes a list of integers as its argument.

The function should return a new list, which contains all
values from the original list doubled. The function should
not change the original list.

An example of the function at work:

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

Sample output
original: [2, 4, 5, 3, 11, -4]
doubled: [4, 8, 10, 6, 22, -8]"""


# Write your solution here
def double_items(numbers: list):
    doubled_numbers = []

    for number in numbers:
        doubled_numbers.append(number * 2)

    return doubled_numbers


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

"""
# Suggested Solution

def double_items(numbers: list):
    double = numbers[:]
    for i in range(len(double)):
        double[i] *= 2
    
    return double

#Review
My solution gives the same output. The suggested one takes a slightly different 
structural approach by first creating a shallow copy of the original list and then 
modifying it in place with indexing. This method emphasizes avoiding mutation of the 
original list through copying, while mine builds a new list from scratch. 

Both are valid, but the suggested approach is a neat reminder of how list slicing 
can be used for safe, in-place transformations.
"""
