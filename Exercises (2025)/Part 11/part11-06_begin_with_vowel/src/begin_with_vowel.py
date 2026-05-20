"""
Please write a function named begin_with_vowel(words: list) which takes a list of strings as its argument.

The function should use a list comprehension technique to create and return a new list, containing only those words from the original list which begin with a vowel (a, e, i, o, u). Both lowercase and uppercase letters should be accepted.

The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

An example of the function in use:

word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)

Sample output
automobile
Animal
APPLE
orange
"""


# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    return [
        word for word in words if word[0].lower() in ["a", "e", "i", "o", "u"]
    ]  # Or by using .startswith("a", "e", "i", "o", "u")


if __name__ == "__main__":
    word_list = ["automobile", "motorbike", "Animal", "cat", "Dog", "APPLE", "orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)

"""
#Suggested solution

def begin_with_vowel(words: list):
    return [word for word in words if word[0].lower() in "aeiou"]
 

#Review
My solution results in the same output, the suggested one is the same
except that it doesn't put the vowels into a list.

"""
