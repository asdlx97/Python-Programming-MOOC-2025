"""
Please write a function named print_many_times(text, times), 
which takes a string and an integer as arguments. 
The integer argument specifies how many times the string argument should be printed out:

print_many_times("hi", 5)

print()

text = "All Pythons, except one, grow up"
times = 3
print_many_times(text, times)

Sample output
hi
hi
hi
hi
hi

All Pythons, except one, grow up.
All Pythons, except one, grow up.
All Pythons, except one, grow up.
"""
# Write your solution here
def print_many_times(string, number):
    print(f"{string}\n" * number)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)

"""
# Suggested solution

def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1
 
if __name__ == "__main__":
    print_many_times("python", 5)

#Review
My solution results in a slightly different output as there is a trailing blank line at
the end because of the '\n' usage. 

#TODO Rewrite own solution and use .rstrip() method to get rid of final trailing line. Or just use while loop as suggested. Or for loop once covered.

""" 