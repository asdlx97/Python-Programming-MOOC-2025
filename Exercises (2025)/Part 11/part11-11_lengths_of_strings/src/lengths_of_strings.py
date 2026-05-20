"""
Please write a function named lengths(strings: list) which takes a list of strings as its argument. The function should return a dictionary with the strings in the list as the keys and their lengths as the values.

The function should be implemented with a dictionary comprehension. The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

The function should work as follows:

word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)

Sample output
{'once': 4, 'upon': 4, 'a': 1, 'time': 4, 'in': 2}
"""

# WRITE YOUR SOLUTION HERE:
def lengths(strings: list):
    return {string:len(string) for string in strings}

if __name__ == "__main__":
    word_list = ["once", "upon" , "a", "time", "in"]

    word_lengths = lengths(word_list)
    print(word_lengths)

"""
#Suggested solution

def lengths(strings: list):
    return {string: len(string) for string in strings}
 

#Review
My solution results in the same output, the suggested one is the same script.
"""
