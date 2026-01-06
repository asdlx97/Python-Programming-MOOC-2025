"""
Please write a module named string_helper, which
contains the following functions:

The function change_case(orig_string: str) creates
and returns a new version of the parameter string.
The lowercase letters in the original should be uppercase,
and uppercase letters should be lowercase.

The function split_in_half(orig_string: str) splits
the parameter string in half, and returns the results
in a tuple. If the original has an odd number of
characters, the first half should be shorter.

The function remove_special_characters(orig_string:
str) returns a new version of the parameter string,
with all special characters removed. Only lowercase
and uppercase letters, numbers and spaces are allowed in the returned string.

Some examples of how the module would be used:

import string_helper

my_string = "Well hello there!"

print(string_helper.change_case(my_string))

p1, p2 = string_helper.split_in_half(my_string)

print(p1)
print(p2)

m2 = string_helper.remove_special_characters("This
is a test, lets see how it goes!!!11!")
print(m2)

Sample output
wELL HELLO THERE!
Well hel
lo there!
This is a test lets see how it goes11
"""

# Write your solution here
from string import ascii_letters, digits


def change_case(orig_string: str):
    return orig_string.swapcase()


def split_in_half(orig_string: str):
    if len(orig_string) % 2 == 0:
        half = int(len(orig_string) / 2)
    else:
        half = int(len(orig_string) // 2)

    return (orig_string[0:half], orig_string[half:])


def remove_special_characters(orig_string: str):
    result = ""
    for letter in orig_string:
        if (
            letter in ascii_letters or letter in digits or letter == " "
        ):  # Didn't work with 'not in punctuation'
            result += letter
        else:
            continue
    return result


if __name__ == "__main__":
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
    p1, p2 = split_in_half("abcd")

    print(p1)
    print(p2)
    print(change_case("Hello World!"))

"""
# Suggested solution

 
from string import ascii_letters, digits
 
def change_case(orig_string: str):
    new_string = ""
    for character in orig_string:
        if character.isupper():
            new_string += character.lower()
        elif character.islower():
            new_string += character.upper()
        else:
            new_string += character
 
    return new_string
 
def split_in_half(orig_string: str):
    return orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:]
 
def remove_special_characters(orig_string: str):
    allowed = ascii_letters + digits + ' '
    new_string = ""
    for character in orig_string:
        if character in allowed:
            new_string += character
 
    return new_string

#Review
My solution results in the same output and slightly more Pythonic (thanks to swapcase()), 
though I could simplify split_in_half() and remove redundant checks there.
"""
