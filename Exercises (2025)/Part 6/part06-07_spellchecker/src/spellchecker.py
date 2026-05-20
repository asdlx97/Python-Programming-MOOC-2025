"""
Please write a program which asks the user to type in some text.
Your program should then perform a spell check, and print out feedback
to the user, so that all misspelled words have stars around them.

Please see the two examples below:

Sample output
Write text: We use ptython to make a spell checker
We use *ptython* to make a spell checker

Sample output
Write text: This is acually a good and usefull program
This is *acually* good and *usefull* program
The case of the letters should be irrelevant to the functioning of your program.

The exercise template includes the file wordlist.txt, which contains all the words
 the spell checker should accept as correct.

NB: this exercise doesn't ask you to write any functions, so you should not place
 any code within an if __name__ == "__main__" block.

NB2 If Visual Studio can't find the file and you have checked that there are no
spelling errors, take a look at these instructions.
"""

# write your solution here
known_words = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        known_words.append(line)

some_text = input("Write text: ").split(" ")

output = ""

for word in some_text:
    if word.lower() in known_words:
        output += f"{word} "
    else:
        output += f"*{word}* "

print(output.strip())

"""
# Suggested solution

def wordlist():
    words = []
 
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
 
    return words
 
words = wordlist()

sentence = input("Write text: ")
 
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "* ", end="")
 
print()
    
#Review
My solution produces the same output, altough exercise brief suggests functions
aren't expected, suggested solution the suggested solution simply moves the 
wordlist-loading logic into a helper function (wordlist()), 
which is a nice modular improvement.
 """
