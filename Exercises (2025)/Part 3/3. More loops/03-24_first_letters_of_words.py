"""
Please write a program which asks the user to type in a sentence. 
The program then prints out the first letter of each word in the sentence, 
each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w

"""
# Write your solution here
sentence = input("Please type in a sentence: ")
i = 1

print(sentence[0]) #We can already print first letter (of first word)

# while i <= len(sentence): #This would give an indexing error when sentence ends with extra " "
while i < len(sentence):
    if sentence[i-1] == " " and sentence[i] != " ": #Also check if sentence doesn't contain succeeding spaces
        print(sentence[i])

    i += 1

"""
# Suggested solution

sentence = input("Please type in a sentence: ")
 
# Add a space at the start, to make handling sentence easier
sentence = " " + sentence
 
# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1

#Review
My solution results in the same output. But had to fix possible indexing error. 
Additionally fixed possible scenario where there are two " " 
right after eachother within the sentence.

""" 