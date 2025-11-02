"""
Please write a function named squared, which takes a string argument and an integer argument, 
and prints out a square of characters as specified by the examples below.

squared("ab", 3)
print()
squared("aybabtu", 5)

Sample output
aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba
"""
# Write your solution here
def squared(string,lines):
    #Make sure our string is long enough not to encounter index problems when slicing
    if len(string) < lines:
        multiplier = ((lines - len(string))*lines) + lines
    else:
        multiplier = lines
    full_pattern = string * multiplier

    #Debug print
    # print(full_pattern)

    #Set loop counter
    current_line = 1
    #Set slicing starting point
    slice_start = 0
    #Set slicing endpoint
    slice_end = lines

    while current_line <= lines:
        print(full_pattern[slice_start:slice_end])
        slice_end += lines
        slice_start += lines
        current_line += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)

"""
# Suggested solution

def squared(characters, size):
    i = 0
    row = ""
    while i < size * size: #Counter for all characters in the grid
        if i > 0 and i % size == 0: #Detect end of row, every time the modulo hits zero, we hit end of the line of given size
            print(row) #Output finished line
            row = "" #Start fresh line
        row += characters[i % len(characters)] #Collects one letter at a time using modulo for index
        i += 1
    print(row) #After the loop it prints last row

#Review
My solution results in the same output. But the suggested one using modulo 
is such a simple and brilliant way to cycle through the whole matrix!! 
Will definitely remember this one as it creates infinite loops through a finite range

Mine builds the full patern first instead of on the fly, end therefor uses slightly more memory
as it results in extra padding sometimes. But my logic is maybe slightly easier to understand (for beginners like me :)
""" 