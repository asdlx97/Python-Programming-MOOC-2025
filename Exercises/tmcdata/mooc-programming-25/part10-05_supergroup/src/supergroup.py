"""
The exercise template contains the class definition for a SuperHero.

Please define a class named SuperGroup which represents a group of superheroes. The class should contain the following members:

Protected attributes name (str), location (str) and members (list)
A constructor which takes the name and location of the group as arguments, in that order
Getter methods for the name and location attributes
A method named add_member(hero: SuperHero) which adds a new member to the group
A method named print_group which prints out information about the group and its members, following the format specified below
An example of the class in action:

superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
invisible = SuperHero("Invisible Inca", "Invisibility")
revengers = SuperGroup("Revengers", "Emerald City")

revengers.add_member(superperson)
revengers.add_member(invisible)
revengers.print_group()

Sample output
Revengers, Emerald City
Members:
SuperPerson, superpowers: Superspeed, superstrength
Invisible Inca, superpowers: Invisibility
If you need a refresher on getter and setter methods, please have a look at this section in the previous part of the material.
"""


# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f"{self.name}, superpowers: {self.superpowers}"


class SuperGroup(SuperHero):
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._members = []

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def __str__(self):
        return f"{self.name}, {self.location}"

    def print_group(self):
        print(self)
        print("Members:")
        for hero in self._members:
            print(hero)  # As str method already exists in the SuperHero class


if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()

"""
# Suggested solution

class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers
 
    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'
 
class SuperGroup:
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []
 
    @property
    def name(self):
        return self._name
 
    @property
    def location(self):
        return self._location
 
    def add_member(self, superhero: SuperHero):
        self._members.append(superhero)
 
    def print_group(self):
        print(f"{self.name}, {self.location}")
        print("Members:")
        for member in self._members:
            print(member)

#Review
My solution results in the same output, the suggested one 
has the same script.