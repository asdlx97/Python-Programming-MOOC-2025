"""
The exercise template contains the file words.txt, which
contains some English language words, one on each line.

Please write a function named words(n: int, beginning:
str), which returns a list containing n random words
from the words.txt file. All words should begin with
the string specified by the second argument.

The same word should not appear twice in the list. If
there are not enough words beginning with the specified
string, the function should raise a ValueError exception.

An example of the function in action:

word_list = words(3, "ca")
for word in word_list:
    print(word)

Sample output
cat
car
carbon
"""

# Write your solution here
from random import sample


def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as new_file:
        for word in new_file:
            word_list.append(word.strip())

    validated_words = []
    for word in word_list:
        if word not in validated_words and word.startswith(beginning):
            validated_words.append(word)

    return sample(validated_words, n)


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)

"""
# Suggested solution

import random
 
def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError("Not enough suitable 
        words can be found!")
    return random.sample(word_list, n)

#Review
My solution results in the same output. The main structural 
difference is that I first collect all words and then filter 
them in a second loop, while the suggested version filters 
directly during reading. This makes my version slightly less 
efficient but equally clear.

One minor improvement would be to include a ValueError check 
if there aren’t enough matching words — the suggested version 
explicitly raises an error, while mine currently assumes enough words exist.
"""
