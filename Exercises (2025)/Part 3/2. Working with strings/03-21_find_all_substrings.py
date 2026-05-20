"""
Please make an extended version of the previous program, 
which prints out all the substrings which are at least three characters long, 
and which begin with the character specified by the user. 

You may assume the input string is at least three characters long.

Sample output
Please type in a word: mammoth
Please type in a character: m
mam
mmo
mot

Sample output
Please type in a word: banana
Please type in a character: n
nan

Hint the following example may give you some inspiration as to how this exercise could be tackled:

word = input("Word: ")
while True:
    if len(word) == 0:
        break
    print(word)
    word = word[2:]

Sample output
Word: mammoth
mammoth
mmoth
oth
h

"""
# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
counter = 0

while counter < len(word):
    if word[counter] == character and counter+3 <= len(word):
        print(word[counter:counter+3])
        

    counter += 1

"""
# Suggested solution

word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1

#Review
My solution results in the same output, but suggested one seems slightly more optimized as
it checks for the possible length of the slice in the loop condition which results in 
fewer iterations.

#TODO Rewrite this using a for loop with the range() function later on when covered in course
""" 


