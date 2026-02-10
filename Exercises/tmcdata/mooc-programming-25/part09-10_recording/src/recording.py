"""
Please create a class named Recording which models a single recording. The class should have one private variable: __length of type integer.

Please implement the following:

a constructor which takes the length as an argument
a getter method length which returns the length of the recording
a setter method which sets the length of the recording
It should be possible to make use of the class as follows:

the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)

Sample output
43
44
If the argument for either the constructor or the setter method is below zero, this should raise a ValueError.

If you need a refresher on raising exceptions, please see part 6 of the course materials.
"""


# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length cannot be under zero.")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, meters: int):
        if meters >= 0:
            self.__length = meters
        else:
            raise ValueError("The length cannot be under zero.")


if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
    the_wall.length = 0
    print(the_wall.length)
    the_wall.length = -3
    print(the_wall.length)

"""
# Suggested solution

class Recording:
    def __init__(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Negative length is not possible")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("Negative length is not possible")

#Review
My solution results in the same output, suggested one follows
the same script.
"""
