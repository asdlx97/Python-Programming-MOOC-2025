"""
Please write a function named new_person(name: str, age: int),
which creates and returns a tuple containing the data in the arguments.
The first element should be the name and the second the age.

If the values stored in the parameter variables are not valid,
the function should throw a ValueError exception.

Invalid parameters in this case include:

name is an empty string
name contains less than two words
name is longer than 40 characters
age is a negative number
age is greater than 150
"""


# Write your solution here
def new_person(name: str, age: int):
    if len(name.split()) < 2 or name == "" or len(name) > 40 or age < 0 or age > 150:
        raise ValueError("The input was invalid: " + str(name) + " " + str(age))

    return (name, age)


if __name__ == "__main__":
    print(new_person("Arno Del", 8))

"""
# Suggested solution

 
def new_person(name: str, age: int):
    # Validate name
    if name == "" or (" " not in name) or len(name) > 40:
        raise ValueError("Invalid argument value for name: " + name)
 
    # Validate age
    if age < 0 or age > 150:
        raise ValueError("Invalid argument value for age:" + str(age))
 
    # Both ok
    return (name, age)
 
 
#Review
My solution returns the same output, suggested one validates name and ages separately.
 """
