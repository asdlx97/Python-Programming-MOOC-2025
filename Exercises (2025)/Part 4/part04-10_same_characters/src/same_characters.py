"""
Please write a function named same_chars, 
which takes one string and two integers as arguments. 
The integers refer to indexes within the string. 
The function should return True if the two characters at the indexes specified are the same. 

Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

Some examples of how the function is used:

# same characters m and m
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False
"""

# Write your solution here
def same_chars(string, first_index, second_index):
    if first_index >= len(string) or second_index >= len(string):
        return False
    elif string[first_index] != string[second_index]:
        return False
    else:
        return True



# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))

"""
# Suggested Solution

def same_chars(str, a, b):
    if a >= len(str) or b >= len(str):
        return False
    return str[a] == str[b]

#Review
My suggestion results in the same output. Suggested is a bit shorter and pythonic as
it just returns the boolean produced by the expression :) I'll try to use this too in the future
"""