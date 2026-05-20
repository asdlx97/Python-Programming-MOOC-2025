"""
Please write a function named palindromes, 
which takes a string argument and returns True if the string is a palindrome. 
Palindromes are words which are spelled exactly the same backwards and forwards.

Please also write a main program which asks the user to type in words until 
they type in a palindrome:

Sample output
Please type in a palindrome: python
that wasn't a palindrome
Please type in a palindrome: java
that wasn't a palindrome
Please type in a palindrome: oddoreven
that wasn't a palindrome
Please type in a palindrome: neveroddoreven
neveroddoreven is a palindrome!

NB:, the main program should not be 
within an if __name__ == "__main__": block
"""

# Write your solution here
def palindromes(word: str):
    j = -1
    palindrome = True

    for i in range(0, len(word)):
        if word[i] != word[j]:
            palindrome = False
            break
        j -= 1
    
    return palindrome

while True:
    answer = input("Please type in a palindrome: ")
    
    if palindromes(answer):
        print(f"{answer} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

"""
# Suggested Solution

def palindromes(word: str):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True
 
while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(word, "is a palindrome!")
        break
    print("that wasn't a palindrome")

#Review
My solution results in the same output but the suggested one
is less resource intensive as it only checks half of the given string
which makes totally sense!! 
"""

# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":
# block!

