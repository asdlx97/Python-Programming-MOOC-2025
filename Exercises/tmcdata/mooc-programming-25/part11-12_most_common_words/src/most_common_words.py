"""
Please write a function named most_common_words(filename: str, lower_limit: int) which takes a filename and an integer value for a lower limit as its arguments. The function should return a dictionary containing the occurrences of the words which appear at least the number of times specified in the lower_limit parameter.

For example, say the function was used to process a file named comprehensions.txt with the following contents:

List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and loops for creating list.
However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.
When the function is called with the arguments most_common_words("comprehensions.txt", 3) it should return

Sample output
{'comprehension': 4, 'is': 3, 'and': 3, 'for': 3, 'list': 4, 'in': 3}
NB: the case of letters affects the results, and all inflected forms are unique words in this exercise. That is, the words List, lists and list are each separate words here, and only list has enough occurrences to make it to the returned list. All punctutation should be removed before counting up the occurrences.

It is up to you to decide how to implement this. The easiest way would likely be to make use of list and dictionary comprehensions.
"""

# WRITE YOUR SOLUTION HERE:
# def most_common_words(filename: str, lower_limit: int):
#     wordlist = []
#     with open(filename) as new_file:
#         for line in new_file:
#This would only return one line in a list, could repeat and append but then we get a matrix
#             wordlist = [word.strip().replace(".", "").replace(",", "") for word in line.strip().split(" ")]
#     print(wordlist)

# #This would return a list of words, but there will be duplicates
# def most_common_words(filename: str, lower_limit: int):
#     wordlist = []
#     with open(filename) as new_file:
#         wordlist = [word.strip().replace(".", "").replace(",", "").lower() for word in new_file.read().strip().replace("\n", " ").split(" ")]

#Returning a dict immediately with the no of occurences using count(), so no duplicates to be found
def most_common_words(filename: str, lower_limit: int):
    wordlist = []
    with open(filename) as new_file:
        wordlist = [word.strip().replace(".", "").replace(",", "") for word in new_file.read().strip().replace("\n", " ").split(" ")] 
    return {word:wordlist.count(word) for word in wordlist if wordlist.count(word) >= lower_limit}

if __name__ == "__main__":    
    most_common_words("comprehensions.txt", 3)
        
"""
#Suggested solution

from string import punctuation
 
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        content = f.read()
 
        # remove line breaks and punctuation
        content = content.replace("\n", " ")
        for punctuation_mark in punctuation:
            content = content.replace(punctuation_mark, "")
 
        words = content.split(" ")
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}
 
 
# WRITE YOUR SOLUTION HERE:
 
#Review
My solution results in the same output, the suggested imports the punctuation method
from the string module to remove them. It also doesn't use a primary list comprehension
to get the words into a list, before moving on to the dict comprehension.
"""
