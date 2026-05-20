"""
Please familiarize yourself with the Python module
fractions. Use it to write a function named
fractionate(amount: int), which takes the number
of parts as its argument. The function should divide
the number 1 into as many equal sized fractions as
is specified by the argument, and return these in a list.

An example of the function in action:

for p in fractionate(3):
    print(p)

print()

print(fractionate(5))
Sample output
1/3
1/3
1/3

[Fraction(1, 5), Fraction(1, 5), Fraction(1, 5),
Fraction(1, 5), Fraction(1, 5)]
"""

# Write your solution here
from fractions import Fraction


def fractionate(amount: int):
    number = f"1/{amount}"
    fraction = Fraction(number)
    result = []

    for i in range(0, amount):
        result.append(fraction)

    return result


if __name__ == "__main__":
    print(fractionate(5))

"""
# Suggested solution

 
 
from fractions import Fraction
 
def fractionate(amount: int):
    # numerator, denominator
    fraction = Fraction(1, amount)
 
    return [fraction] * amount

#Review
Same output, the suggested version directly uses 
Fraction(1, amount), which is simpler and avoids 
unnecessary string handling. I just didn't know one
could define a Fraction that way directly.
"""
