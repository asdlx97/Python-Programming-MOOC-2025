"""
In this exercise you will write an improved version of the
Spell checker from the previous part.

Just like in the previous version, the program should ask
the user to type in a line of text. Your program should then
perform a spell check, and print out feedback to the user,
so that all misspelled words have stars around them.
Additionally, the program should print out a list
of suggestions for the misspelled words.

Please have a look at the following two examples.

Sample output
write text: We use ptython to make a spell checker
We use *ptython* to make a spell checker
suggestions:
ptython: python, pythons, typhon
Sample output
write text: this is acually a good and usefull program
this is *acually* a good and *usefull* program
suggestions:
acually: actually, tactually, factually
usefull: usefully, useful, museful
The suggestions should be determined with the function
get_close_matches from the Python standard library module difflib.

NB: For the automatic tests to work correctly, please use
the function with the "default settings". That is, please
pass only two arguments to the function: the misspelled word, and the word list.
"""

# Write your solution here
from difflib import get_close_matches

known_words = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        known_words.append(line)

some_text = input("Write text: ").split(" ")

output = ""

suggestions = {}

for word in some_text:
    if word.lower() in known_words:
        output += f"{word} "
    else:
        output += f"*{word}* "
        suggestions[word] = get_close_matches(word, known_words)

print(output.strip())
print("suggestions:")
for key, value in suggestions.items():
    print(f"{key}: {', '.join(value)}")
print()


"""
# Suggested solution

import difflib 
 
def wordlist():
    words = []
    with open("wordlist.txt") as file:
        for rivi in file:
            words.append(rivi.strip())
    return words
 
words = wordlist()
sentence = input("write text: ")
error = []
for word in sentence.split(' '):
    if word.lower() in words:
        print(word+ " ", end="")
    else:
        error.append(word)
        print("*" + word+ "* ", end="") 
 
print()
 
print("suggestions:")
for word in error:
    suggestion_list = difflib.get_close_matches(word, words)
    suggestions = ", ".join(suggestion_list)
    print(f"{word}: {suggestions}")

#Review
My solution results in the same output. 
"""
