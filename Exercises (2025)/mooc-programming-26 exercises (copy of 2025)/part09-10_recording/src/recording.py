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
