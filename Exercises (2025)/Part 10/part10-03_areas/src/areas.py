"""
The exercise template contains a class definition for a Rectangle. It represents a rectangle shape. A Rectangle works like this:

rectangle = Rectangle(2, 3)
print(rectangle)
print("area:", rectangle.area())

Sample output
rectangle 2x3
area: 6
Square

Please define a class named Square which inherits the Rectangle class. The sides of a square are all of equal length, which makes the square a special case of the rectangle. The new class should not contain any new attributes.

A Square object is used as follows:

square = Square(4)
print(square)
print("area:", square.area())

Sample output
square 4x4
area: 16
"""


# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self):
        return f"square {self.width}x{self.height}"


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    print(rectangle)
    print("area:", rectangle.area())

    square = Square(4)
    print(square)
    print("area:", square.area())

"""
The exercise template contains class definitions for a ComputerGame and a GameWarehouse. A GameWarehouse object is used to store ComputerGame objects.

Please familiarize yourself with these classes. Then define a new class named GameMuseum which inherits the GameWarehouse class.

The GameMuseum class should override the list_games() method, so that it returns a list of only those games which were made before the year 1990.

The new class should also have a constructor which calls the constructor from the parent class GameWarehouse. The constructor takes no arguments.

You may use the following code to test your implementation:

museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
for game in museum.list_games():
    print(game.name)

Sample output
Pacman
Bubble Bobble
"""


# TEE RATKAISUSI TÄHÄN:
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year


class GameWarehouse:
    def __init__(self):
        self.games = []

    def add_game(self, game: ComputerGame):
        self.games.append(game)

    def list_games(self):
        return self.ames


class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        filtered_list = []
        for game in self.games:
            if game.year <= 1990:
                filtered_list.append(game)
        return filtered_list


if __name__ == "__main__":
    museum = GameMuseum()
    museum.add_game(ComputerGame("Pacman", "Namco", 1980))
    museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
    museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
    for game in museum.list_games():
        print(game.name)

"""
# Suggested solution

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
 
    def __str__(self):
        return f"rectangle {self.width}x{self.height}"
 
    def area(self):
        return self.width * self.height
 
class Square(Rectangle):
    def __init__(self, side: int):
        # Provide the side as width and height for the
        # superclass constructor
        super().__init__(side, side)
 
    def __str__(self):
        return f"square {self.width}x{self.width}"

#Review
My solution results in the same output, the suggested script is
the same, surprisingly also the usef variable name 'side'.
"""
