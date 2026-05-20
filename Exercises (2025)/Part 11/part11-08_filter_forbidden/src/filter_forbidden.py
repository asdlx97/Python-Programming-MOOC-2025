"""
Please write a function named filter_forbidden(string: str, forbidden: str) which takes two strings as its arguments. The function should return a new version of the first string. It should not contain any characters from the second string.

The function should be implemented using list comprehensions. The maximum length of the function is three lines of code, including the header line beginning with the def keyword.

Please have a look at the example below.

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)

Sample output
Once upon a time there was a python
"""

# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return "".join([letter for letter in string if letter not in forbidden])


if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)

"""
#Suggested solution

def filter_forbidden(string: str, forbidden: str):
    return "".join([character for character in string if character not in forbidden])
 

#Review
My solution results in the same output, the suggested one is the same script.

"""