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
     