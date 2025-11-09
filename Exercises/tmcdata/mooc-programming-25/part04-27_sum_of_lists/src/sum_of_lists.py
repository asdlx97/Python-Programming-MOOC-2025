"""
Please write a function named list_sum which takes 
two lists of integers as arguments. 

The function returns a new list which contains the sums of 
the items at each index in the two original lists. 

You may assume both lists have the same number of items.

An example of the function at work:

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]
"""

# Write your solution here
def list_sum(list1: list, list2: list):
    sum_list = []

    for number in range(0, len(list1)):
        sum = list1[number] + list2[number]

        sum_list.append(sum)
    
    return sum_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))

"""
# Suggested Solution

def list_sum(list1: list, list2: list):
    results = []
    for i in range(len(list1)):
        results.append(list1[i] + list2[i])
 
    return results
# Another solution would be use zip-function,
# which creates new list by combining items in two or more lists
# for item1, item2 in zip(list1, list2):
#   results.append(item1 + item2)
# Write your solution here

#Review
Same output, same script!! 
"""