"""
Please write a class named Person with a single attribute name,
which is set with an argument given to the constructor.

Please also add two methods:

The method return_first_name should return the first name of the
person, while the method return_last_name should return the last name of the person.

You may assume that the name passed to the constructor will
contain exactly two name elements separated with a space character.

An example use case:

if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())
Sample output
Peter
Pythons
Paula
Pythonnen
"""


# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.name = name

    def return_first_name(self):
        return self.name.split(" ")[0]

    def return_last_name(self):
        return self.name.split(" ")[1]


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())

"""
# Suggested solution

class Person:
    def __init__(self, name: str):
        self.name = name
 
    def return_first_name(self):
        names = self.name.split(" ")
        return names[0]
 
    def return_last_name(self):
        names = self.name.split(" ")
        return names[-1]


#Review
My solution results in the same output, suggested one is 
a bit more flexible if user would input a middle name.
"""
