"""Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

You can assume the string will contain only characters from the lowercase English alphabet a...z.

An example of expected behaviour:

my_string = "this is an example"
print(no_vowels(my_string))

Sample output
ths s n xmpl"""


# Write your solution here
def no_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]

    for character in my_string:
        if character in vowels:
            my_string = my_string.replace(character, "")

    return my_string


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

"""
# Suggested Solution

def no_vowels(my_string: str):
    vowels = "aeiou"
    result = ""
 
    for letter in my_string:
        if letter not in vowels:
            result += letter
 
    return result

#Review
My solutions results in the same output, the suggested one doesn't use a list to store the vowels,
and collects the characters that are no vowels into a new string variable, while I replace them in the input string.
"""
