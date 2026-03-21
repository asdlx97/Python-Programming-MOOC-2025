"""
Please write a generator function named even_numbers(beginning: int, maximum: int) which takes two integers as its arguments. The function should produce even numbers starting from beginning and ending with, at most, maximum.

Two examples of how the function works:

numbers = even_numbers(2, 10)
for number in numbers:
    print(number)
Sample output
2
4
6
8
10
numbers = even_numbers(11, 21)
for number in numbers:
    print(number)
Sample output
12
14
16
18
20
"""


# Write your solution here
def even_numbers(beginning: int, maximum: int):
    while beginning <= maximum:
        if beginning % 2 == 0:
            yield beginning
            beginning += 1
        else:
            beginning += 1

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    print()

    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)

"""
#Suggested solution

def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2

#Review
My solution results in the same output, the suggested one takes a slightly different approach
as it is more logical to add 2 to the counter after yielding to get to the next odd number.
"""