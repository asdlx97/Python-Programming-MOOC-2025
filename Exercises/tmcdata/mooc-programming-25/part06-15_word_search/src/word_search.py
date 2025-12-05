"""
The exercise template includes the file words.txt, which contains words in English.

Please write a function named find_words(search_term: str). It should return a list
containing all the words in the file which match the search term.

The search term may include lowercase letters and the following wildcard characters:


A dot . means that any single character is acceptable in its place. For example,
ca. would yield words like cat and car, p.ng would yield words like ping and pong,
and .a.e would yield words like sane, care and late.

An asterisk * at the end of the search term means that any word which begins with
the search term is acceptable. An asterisk at the beginning of the search term means
that any word which ends with the search term is acceptable. For example, ca* would
yield words like california, cat, caring and catapult, while *ane would yield
words like crane, insane and aeroplane. There can only ever be a single asterisk
in the search term.

If there are no wildcard characters in the search term, only words which match the
search term exactly are returned.
You may assume both wildcards are never used in the same search term.

The words in the file are all written in lowercase. You may also assume the argument to the function will be in lowercase entirely.

If no matching words are found, the function should return an empty list.

Hint: the Pythons string methods startswith() and endswith() may be useful here. You can search for more information about them online.

An example of the function in action:

print(find_words("*vokes"))

Sample output
['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']
"""


# Write your solution here
# Store english words from words.txt
def store_words(file: str):
    word_list = []
    with open(file) as new_file:
        for line in new_file:
            word_list.append(line.strip().lower())
    return word_list


# Search for words if inludes dot wildcard
def dot_wildcard(word_list: list, given_word: str):
    word_list = store_words(word_list)
    matching_words = []

    for entry in word_list:
        if len(entry) != len(given_word):
            continue
        match = False
        i = 0
        for character in given_word:
            if character == ".":
                i += 1
                continue
            elif given_word[i] == entry[i]:
                i += 1
                match = True
            else:
                match = False

        if match:
            matching_words.append(entry)

    return matching_words


# Search for words if includes * wildcard
def asterix_wildcard(word_list: list, given_word: str):
    word_list = store_words(word_list)
    matching_words = []

    if given_word.startswith("*"):
        search_term = given_word.strip("*")
        for entry in word_list:
            if entry.endswith(search_term):
                matching_words.append(entry)

    if given_word.endswith("*"):
        search_term = given_word.strip("*")
        for entry in word_list:
            if entry.startswith(search_term):
                matching_words.append(entry)

    return matching_words


def no_wildcard(word_list: list, given_word: str):
    word_list = store_words(word_list)
    matching_words = []

    for entry in word_list:
        if entry == given_word:
            matching_words.append(entry)

    return matching_words


# Defining main function
def find_words(search_term: str):
    filename = "words.txt"
    matching_words = []

    if "*" in search_term:
        matching_words = asterix_wildcard(filename, search_term)
    elif "." in search_term:
        matching_words = dot_wildcard(filename, search_term)
    else:
        matching_words = no_wildcard(filename, search_term)

    return matching_words


if __name__ == "__main__":
    # filename = "words.txt"
    # print(dot_wildcard("words.txt", "a.h"))  # Works!!
    # print(asterix_wildcard("words.txt", "*vokes"))  # Works!!
    print(find_words("*vokes"))

"""
# Suggested solution


def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        # Tätä tarvitaan myöhemmin
        hakusana_ilman_tahtea = search_term.replace("*","")
 
        for word in file:
            word = word.replace("\n","")
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(hakusana_ilman_tahtea):
                        results.append(word)
                else:
                    if word.startswith(hakusana_ilman_tahtea):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results
 

#Review
My solution works correctly for all wildcard and exact match cases and produces 
the same output as the suggested one. Structurally, though, it’s more complex: 
I split the logic into multiple helper functions (store_words, dot_wildcard, 
asterix_wildcard, no_wildcard), which improves readability but causes the word 
file to be read multiple times unnecessarily. The suggested version handles 
everything within a single loop, making it more efficient and compact while still 
easy to follow.
 """
