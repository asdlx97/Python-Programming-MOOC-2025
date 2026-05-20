"""
Please write a function named anagrams, 
which takes two strings as arguments. 

The function returns True if the strings are anagrams of each other. 
Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False
Hint: the function sorted can be used on strings as well.
"""

# Write your solution here
def anagrams(word1: str, word2: str):
    return sorted(word1) == sorted(word2)

if __name__ == "__main__":
    print(anagrams("tame", "meta"))

"""
# Suggested Solution

def anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)

#Review
Same script, same output. 
"""