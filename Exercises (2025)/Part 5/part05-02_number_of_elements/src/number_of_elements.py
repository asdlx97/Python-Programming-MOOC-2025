"""Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.

An example of how the function should work:

m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))

Sample output
3"""


# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    n_matches = 0

    for row in my_matrix:
        for item in row:
            if item == element:
                n_matches += 1

    return n_matches


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))

"""
# Suggested Solution

def count_matching_elements(my_matrix: list, elements: int):
    n = 0
    for row in my_matrix:
        for cell in row:
            if cell == elements:
                n += 1
    return n

#Review
same output, same script.
"""
