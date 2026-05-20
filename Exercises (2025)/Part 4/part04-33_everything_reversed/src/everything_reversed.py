"""Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.

An example of how the function should work:

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
Sample output
['erom eno', 'elpmaxe', 'ereht', 'iH']"""


# Write your solution here
def everything_reversed(my_list: list):
    reversed_list = []

    for word in my_list[::-1]:
        reversed_list.append(word[::-1])

    return reversed_list


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

"""
# Suggested Solution

def everything_reversed(my_list: list):
    new_list = []
    for my_string in my_list:
        new_list.append(my_string[::-1])
    return new_list[::-1]

#Review
My solutions results in the same output, the only difference
is that the suggested one reverses the new list at the end,
while I do that while looping through it.
"""
