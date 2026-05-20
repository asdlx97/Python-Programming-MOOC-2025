"""Please write a function named length_of_longest, 
which takes a list of strings as its argument. 

The function returns the length of the longest string.

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)
Sample output
8
7"""

# Write your solution here
def length_of_longest(my_list: list):
    longest = my_list[0]

    for word in my_list:
        if len(word) > len(longest):
            longest = word

    return len(longest)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)

"""
# Suggested Solution

def length_of_longest(names: list):
    longest = 0
 
    for name in names:
        if len(name) > longest:
          longest = len(name)
 
    return longest

#Review
My solution resulted in the same outpur, I however worked with the names in the list
itself and then returned the len of the longest name in the end. 

For me it's better to be able to print out the longest word itself too, if needed.
"""