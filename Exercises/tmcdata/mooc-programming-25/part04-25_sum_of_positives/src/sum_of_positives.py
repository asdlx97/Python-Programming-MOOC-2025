# Write your solution here
def sum_of_positives(my_list: list):
    sum = 0

    for number in my_list:
        if number >= 0:
            sum += number

    return sum


"""
# Suggested Solution

def sum_of_positives(my_list: list):
    sum = 0
    for item in my_list:
        if item > 0:
            sum += item
    return sum

#Review
Same output, same script!! 
"""
