"""
Please write a program which functions as a dictionary.
The user can type in new entries or look for existing entries.

The program should work as follows:

Sample output
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: auto
The word in English: car
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: roska
The word in English: garbage
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: laukku
The word in English: bag
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: bag
roska - garbage
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: car
auto - car
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: laukku
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 3
Bye!

The dictionary entries should be written to a file called dictionary.txt.
The program should first read the contents of the file. New entries are written
to the end of the file whenever they are added to the dictionary.

The format of the data stored in the dictionary is up to you.

NB: the automatic tests for this exercise may change the contents of the file.
If you want to keep its contents, first make a copy of the file under a different
name.

NB2: this exercise doesn't ask you to write any functions, so you should not
place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
dictionary = {}
# read_dictionary:
with open("dictionary.txt") as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        dictionary[parts[0]] = parts[1]

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))

    if function == 1:
        finnish_word = input("The word in Finnish: ").lower()
        english_word = input("The word in English: ").lower()
        dictionary[finnish_word] = english_word
        print("Dictionary entry added")
    elif function == 2:
        search_term = input("Search term: ").lower()
        for key, value in dictionary.items():
            if search_term in key or search_term in value:
                print(f"{key} - {value}")
    elif function == 3:
        with open("dictionary.txt", "w") as new_file:
            for key, value in dictionary.items():
                new_file.write(f"{key};{value}\n")
        print("Bye!")
        break

"""
# Suggested solution


def read_dictionary():
    # Words are stored in a list. If the translation would always
    # be to same direction (e.g. from English to Finnish),
    # using dictionary as a data structure would be a good idea
    dictionary = []
 
    with open("dictionary.txt") as file:
        # In the example file, word pair is at one line as
        # finnish;english, for example
        # auto;car
        for row in file:
            row = row.replace("\n","")
            dictionary.append(tuple(row.split(";")))
 
    return dictionary
 
def add_word(dictionary: list):
    word_fi = input("The word in Finnish: ")
    word_en = input("The word in English: ")
    # Add to list
    dictionary.append((word_fi, word_en))
 
    # Write to file
    with open("dictionary.txt", "a") as file:
        file.write(word_fi + ";" + word_en + "\n")
        print("Dictionary entry added")
 
def search_word(dictionary: list):
    word = input("Search term: ")
    for word_fi, word_en in dictionary:
        if word in word_fi or word in word_en:
            print(f"{word_fi} - {word_en}")
 
 
dictionary = read_dictionary()
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        add_word(dictionary)
    elif function == "2":
        search_word(dictionary)
    elif function == "3":
        print("Bye!")
        break
 

#Review
My solution works correctly — it loads the dictionary file, allows adding and 
searching words, and saves updates back to dictionary.txt before quitting. 
Functionally, it behaves exactly as required.

Structurally, the suggested version separates the logic into helper functions 
(read_dictionary, add_word, search_word), making it cleaner and easier to maintain.
I kept everything inside a single loop because the exercise didn’t require defining 
functions, so i didn't know if it would give an error when checking if I'd use functions.
 """
