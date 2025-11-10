"""Please write a function named all_the_longest, 
which takes a list of strings as its argument. 

The function should return a new list containing the 
longest string in the original list. 

If more than one are equally long, the function should return all of the longest strings.

The order of the strings in the returned list should be the same as in the original.

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result) # ['eleventh']
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']"""

# Write your solution here
def length_of_longest(my_list: list):
    longest = my_list[0]

    for word in my_list:
        if len(word) > len(longest):
            longest = word

    return len(longest)

def all_the_longest(my_list: list):
    len_of_longest = length_of_longest(my_list)

    all_longest = []

    for name in my_list:
        if len(name) == len_of_longest:
            all_longest.append(name)

    return all_longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']

"""
# Suggested Solution

def all_the_longest(names: list):
    result = []
 
    for name in names:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
 
    return result

#Review
My solution resulted in the same output, the suggested one made a new
shorter function to either redefine the longest list when the name is longer,
or append it to the longest list if its the same length. 

My solution uses the function we contructed two exercises ago to find longest
in the list and uses this in a new function to find all names of that length.

"""