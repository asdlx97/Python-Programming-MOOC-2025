"""
Please write a program which asks the user for words. 
If the user types in a word for the second time, 
the program should print out the number of different words typed in, and exit.

Sample output
Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words

NB: this exercise doesn't ask you to write any functions, 
so you should not place any code within an if __name__ == "__main__" block.
"""

# Write your solution here
my_list = []

while True:
    answer = input("Word: ")
    if answer in my_list:
        break
    else:
        my_list.append(answer)

print(f"You typed in {len(my_list)} different words")

"""
# Suggested Solution

words = []
while True:
    word = input("Word: ")
    if word in words:
        break
    words.append(word)
 
print("You typed in", len(words), "different words")

#Review
My suggestion results in the same output. Suggested one doesn't use else statement as it is not needed indeed.
"""