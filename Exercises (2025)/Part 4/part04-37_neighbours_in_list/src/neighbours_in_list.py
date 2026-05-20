"""Given a list of integers, let's decide that two consecutive items in the list are neighbours
if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, which looks for the longest
series of neighbours within the list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

An example function call:

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))

Sample output
4"""


# Write your solution here
def longest_series_of_neighbours(my_list):
    longest_series = []
    i = 0

    while i <= len(my_list) - 2:
        start_index = i
        end_index = start_index + 1

        while end_index < len(my_list):
            difference = abs(my_list[end_index] - my_list[start_index])
            if difference == 1:
                start_index += 1
                end_index += 1
            else:
                break

        if len(my_list[i:end_index]) >= len(longest_series):
            longest_series = my_list[i:end_index]

        i += 1

    return len(longest_series)


if __name__ == "__main__":

    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))

"""
# Suggested Solution

def longest_series_of_neighbours(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest

#Review
My solution produces the same output. The suggested one is structurally simpler, 
using a single loop with counters instead of nested loops and slicing. 
By tracking sequence lengths directly through result and longest, 
it avoids repeatedly creating sublists and keeps the logic straightforward.
"""
