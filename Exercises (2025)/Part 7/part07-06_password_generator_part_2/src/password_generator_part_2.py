"""
Please write an improved version of your password generator.
The function now takes three arguments:

If the second argument is True, the generated password should also
contain one or more numbers.

If the third argument is True, the generated password should also
contain one or more of these special characters: !?=+-()#.

Despite these two additional arguments, the password should always
contain at least one lowercase alphabet. You may assume the function will
only be called with combinations of arguments that are possible to formulate
into passwords following these rules. That is, the arguments will not specify
e.g. a password of length 2 which contains both a number and a special characters,
for then there would not be space for the mandatory lowercase letter.

An example of how the function should work:

for i in range(10):
    print(generate_strong_password(8, True, True))

Sample output
2?0n+u31
u=m4nl94
n#=i6r#(
da9?zvm?
7h)!)g?!
a=59x2n5
(jr6n3b5
9n(4i+2!
32+qba#=
n?b0a7ey
"""

# Write your solution here
from string import ascii_lowercase
from random import randint, choice


def generate_strong_password(length: int, numberneeded: bool, specialneeded: bool):
    pwd = ""
    special_char = ["!", "?", "=", "+", "-", "(", ")", "#"]
    contains_no = False
    contains_spec_char = False

    while len(pwd) < length:
        if numberneeded and not contains_no:
            pwd += str(randint(0, 9))
            contains_no = True
            continue
        if specialneeded and not contains_spec_char:
            pwd += choice(special_char)
            contains_spec_char = True
            continue
        pwd += choice(ascii_lowercase)

    return pwd


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))


"""
# Suggested solution

from random import choice, randint
from string import ascii_lowercase, digits

def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    # One letter at beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase

    # If numbers is wanted, add at least one number
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits

    # same for special characters
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars

    # build the rest of the password from the whole set
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)

    return passwd

# Add a random character from the given set either
# at the beginning or end of the string
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character

#Review
My solution correctly generates strong passwords of the specified length, 
always including at least one lowercase letter, and optionally numbers 
and special characters when required.

However, it always adds mandatory character types in a predictable order 
(numbers and special characters first, then letters), making the structure 
less random. The suggested solution improves this by using a helper function 
add_character() to insert required characters at random positions, increasing 
randomness and security. It also builds a dynamic character set for continued 
password generation, which is more elegant and scalable.
"""
