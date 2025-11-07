"""
Please write a function named  range_of_list, which takes a list of integers as an argument. 
The function returns the difference between the smallest and the largest value in the list.

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list))
print("The range of the list is", result)
Sample output
The range of the list is 4
"""

# Write your solution here
def range_of_list(a_list):
    sorted_list = sorted(a_list)
    return sorted_list[-1] - sorted_list[0]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)

"""
# Suggested Solution

def range_of_list(my_list : list):
    return max(my_list) - min(my_list)

#Review
My solution results in the same output, however the suggested one is more memory efficiënt as
mine has to store and extra variable. Suggested one also reads more naturally.
"""