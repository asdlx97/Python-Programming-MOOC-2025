"""
Please write a function named histogram, which takes a string as its argument.
The function should print out a histogram representing the number of times each
letter occurs in the string. Each occurrence of a letter should be represented
by a star on the specific line for that letter.

For example, the function call histogram("abba") should print out

Sample output
a **
b **
while histogram("statistically") should print out

Sample output
s **
t ***
a **
i **
c *
l **
y *
"""


# Write your solution here
def histogram(my_string: str):
    histograms = {}

    for character in my_string:
        if character not in histograms:
            histograms[character] = []
        histograms[character].append("*")

    for key, value in histograms.items():
        # Probably there is also a way to print the value itself instead of using len() to multiply
        print(f"{key} {'*' * len(value)}")


if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")

"""
# Suggested solution

def histogram(my_str: str):
    characters = {}
    for character in my_str:
        if not character in characters:
            characters[character] = 0
        characters[character] += 1
 
    for character, lkm in characters.items():
        stars = "*"*lkm
        print(f"{character} {stars}")

#Review
My solution produces the same output. Structurally, the suggested one is simpler 
and more memory-efficient — it stores counts as integers instead of lists of stars, 
avoiding unnecessary data buildup. The star strings are created only when printing, 
which keeps the dictionary focused purely on counting.

I thought about doing it this way when reaching line 36 but was already too far in 
and my solution of using value len() was working.
"""
