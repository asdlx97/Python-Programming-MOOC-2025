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

class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year
 
class GameWarehouse:
    def __init__(self):
        self.__games = []
 
    def add_game(self, game: ComputerGame):
        self.__games.append(game)
 
    def list_games(self):
        return self.__games
 
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()
 
    def list_games(self):
        gamelist = []
        for game in super().list_games():
            if game.year < 1990:
                gamelist.append(game)
 
        return gamelist

#Review
My solution results in the same output, but instead of making the 
gamelist of the GameWarehouse class public like I did, the suggested solution
makes uses from the returned list from the list_games() method which makes
sense and means I didn't stury the given classes enough. I think there might
be a way using protected traits which we will cover in the next section of part 10.
"""
