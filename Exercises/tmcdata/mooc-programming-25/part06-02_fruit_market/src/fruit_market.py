"""
The file fruits.csv contains names of fruits, and their prices,
in the format specified in this example:

banana;6.50
apple;4.95
orange;8.0
...etc...

Please write a function named read_fruits, which reads the file and returns
a dictionary based on the contents. In the dictionary, the name of the fruit
should be the key, and the value should be its price. Prices should be of type float.

NB: the function does not take any arguments.
The file you are working with is always named fruits.csv.
"""


# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits = {}

        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            price = float(parts[1])
            fruits[name] = price

        return fruits


if __name__ == "__main__":
    read_fruits()

"""
# Suggested solution

def read_fruits():
    with open("fruits.csv") as file:
        fruits = {}
        for row in file:
            # split to two pieces
            data = row.split(";")
            # name first, price second
            fruits[data[0]] = float(data[1])
    return fruits
    
#Review
Same output, script nearly identical.
 """
