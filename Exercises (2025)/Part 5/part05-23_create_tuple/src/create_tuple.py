"""
Please write a function named create_tuple(x: int, y: int, z: int),
which takes three integers as its arguments, and creates and returns
a tuple based on the following criteria:

The first element in the tuple is the smallest of the arguments
The second element in the tuple is the greatest of the arguments
The third element in the tuple is the sum of the arguments
An example of its use:


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

Sample output
(-1, 5, 7)
"""


# Write your solution here
def create_tuple(x: int, y: int, z: int):
    arguments = (x, y, z)
    # arguments[x, y, z] #This also works

    final_tuple = (min(arguments), max(arguments), sum(arguments))

    return final_tuple


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

"""
# Suggested solution

def create_tuple(x: int, y: int, z: int):
    """ The function returns a tuple formed from the parameters (smallest, greatest, sum) """
    smallest = min([x, y, z])
    greatest = max([x, y, z])
    sum = x + y + z # sum([x, y, z]) also works
 
    return (smallest, greatest, sum)
    
#Review
My solution gives the same correct output and is a bit more concise.
"""
