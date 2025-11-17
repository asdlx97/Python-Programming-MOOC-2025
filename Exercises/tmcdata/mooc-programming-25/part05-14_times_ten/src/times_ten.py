"""
Please write a function named times_ten(start_index: int, end_index: int),
which creates and returns a new dictionary.

The keys of the dictionary should be
the numbers between start_index and end_index inclusive

The value mapped to each key should be the key times ten.

For example:

d = times_ten(3, 6)
print(d)

Sample output
{3: 30, 4: 40, 5: 50, 6: 60}
"""


# Write your solution here
def times_ten(start_index: int, end_index: int):
    new_dictionary = {}

    while start_index <= end_index:
        new_dictionary[start_index] = start_index * 10
        start_index += 1

    return new_dictionary


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)

"""
# Suggested Solution

def times_ten(start_index: int, end_index: int):
    numbers = {}
    for i in range(start_index, end_index + 1):
        numbers[i] = i * 10
    return numbers

#Review
My solution returns the same output, but the suggested one uses
the for loop ranging inbetween both indexes, which makes more sense.

Had a bit hard time thinking about assigning values to keys but got it now.
Didn't read the syntax very well before starting.
"""
