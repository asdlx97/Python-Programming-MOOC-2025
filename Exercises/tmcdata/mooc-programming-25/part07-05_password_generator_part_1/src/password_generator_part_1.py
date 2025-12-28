"""
Please write a function which creates passwords of a desired length,
consisting of lowercase characters a to z.

An example of how the function should work:

for i in range(10):
    print(generate_password(8))
Sample output
lttehepy
olsxttjl
cbjncrzo
dwxqjdgu
gpfdcecs
jabyvgar
xnbbonbl
ktmsjyww
ejhprmel
rjkoacib
"""

# Write your solution here
from string import ascii_lowercase
from random import randint


def generate_password(length: int):
    pwd = ""
    while len(pwd) < length:
        pwd += ascii_lowercase[randint(0, len(ascii_lowercase) - 1)]
    return pwd


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(2))

"""
# Suggested solution

 
from random import choice
from string import ascii_lowercase
 
def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
 
    return passwd

#Review
My solution results in the same output. The main difference lies in style: 
I used randint with indexing to select characters, while the suggested 
solution uses random.choice(), which is cleaner and more Pythonic. 

Both achieve the same randomness, but choice() expresses intent more 
clearly and avoids manual index handling.
"""
