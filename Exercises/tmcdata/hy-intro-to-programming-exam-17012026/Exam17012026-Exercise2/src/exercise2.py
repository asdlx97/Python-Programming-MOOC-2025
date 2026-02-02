# Write your solution to exercise 2 here
def find_allowed(string_list: list, min_desired_letters: int):
    #I like to first initialize the list that I'll return at the end
    approved_words = []

    #I'll populate a new list by appending from the given one, to avoid modifying it as we saw in the course regarding memory references, although not strictly necessary in this case, became a good habit, thanks! 
    given_words = []
    for word in string_list: #I could also use [:] as we saw in the course
        given_words.append(word) 

    desired_letters = "aeiouy"
    for word in given_words:
        amount_of_desired_letters = 0
        for character in word:
            if character in desired_letters:
                amount_of_desired_letters += 1
        if amount_of_desired_letters >= min_desired_letters:
            approved_words.append(word)
    
    return approved_words #Didn't modify any given argument, this is what we call a pure function?

if __name__ == "__main__":
    wordlist = ["apple", "banana", "cherry", "orange", "peach", "pineapple"]
    minimum = 3
    result = find_allowed(wordlist, minimum)
    print(result)


