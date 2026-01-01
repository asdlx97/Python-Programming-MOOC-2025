"""
In this exercise you will validate Finnish Personal Identity Codes (PIC).

Please write a function named is_it_valid(pic: str), which returns True
or False based on whether the PIC given as an argument is valid or not.
Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the
date of birth, X is the marker for century, yyy is the personal identifier
and z is a control character.

The program should check the validity by these three criteria:

The first half of the code is a valid, existing date in the format ddmmyy.
The century marker is either + (1800s), - (1900s) or A (2000s).
The control character is valid.
The control character is calculated by taking the nine-digit number created
by the date of birth and the personal identifier, dividing this by 31, and
selecting the character at the index specified by the remainder from the
string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12,
the control character would be C.

More examples and explanations of the uses of the PIC are available at the
Digital and Population Data Services Agency.

NB! Please make sure you do not share your own PIC, for example in the code
you use for testing or through the course support channels.

Here are some valid PICs you can use for testing:

230827-906F
120488+246L
310823A9877
"""

# Write your solution here
from datetime import datetime, timedelta


def is_it_valid(pic: str):
    is_valid = True
    controle_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    century_markers = {"+": "18", "-": "19", "A": "20"}
    debug_len = len(controle_string)
    # Let's decompose pic for clarity e.g. 230827-906F
    century_marker = pic[6]
    individual_no_and_bd = pic[0:6] + pic[7:10]
    controle_char = pic[10]
    year = int(century_markers[century_marker] + pic[4:6])
    # print(year) #debug
    month = int(pic[2:4])
    day = int(pic[0:2])

    # Check length
    if len(pic) != 11:
        return False

    # Check if date exists
    try:
        correct_date = datetime(year, month, day)
        # print(correct_date) #debug
    except ValueError:
        return False

    # Check century marker is existing
    if century_marker not in century_markers.keys():
        return False

    # Check validity controle character
    index = int(individual_no_and_bd) % 31
    # breakpoint()
    check = controle_string[index]
    if controle_char != check:
        return False

    return True


if __name__ == "__main__":
    print(is_it_valid("100400A644E"))
    print(is_it_valid("230827-906F"))

"""
# Suggested solution

from datetime import datetime
 
def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    numbers = pic[:6]+pic[7:10]
    for x in numbers:
        if x not in "0123456789":
            return False
    century_marker = pic[6]
    if century_marker not in "+-A":
        return False
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    if century_marker == "+":
        year += 1800
    if century_marker == "-":
        year += 1900
    if century_marker == "A":
        year += 2000
    try:
        test = datetime(year, month, day)
    except:
        return False
    characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    index = int(numbers)%31
    return characters[index] == pic[-1]

#Review
My solution results in the same output and maybe slightly more elegant due 
to the century dictionary approach. The suggested solution however adds a
quick numeric character check that makes it more robust.
"""
