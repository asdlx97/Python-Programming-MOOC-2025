"""Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

An example of expected behaviour:

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))
Sample output
b
e"""


# Write your solution here
def most_common_character(my_string: str):
    most_occuring = " "

    for character in my_string[::-1]:
        if my_string.count(character) >= my_string.count(most_occuring):
            most_occuring = character

    return most_occuring


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

"""
# Suggested Solution

def most_common_character(my_string: str):
    most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
            most_common = character
 
    return most_common

#Review
My solutions results in the same output, the suggested one doesn't reverses the string
when looping through it, which makes sense as it uses the > operator.

I thought I had to reverse it to start from the end in order to make sure
I get the first most recurring character if there are multiple ones. But I was wrong, it isn't needed.
"""
