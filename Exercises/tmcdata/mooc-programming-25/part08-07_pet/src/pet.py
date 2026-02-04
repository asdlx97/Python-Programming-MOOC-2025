"""
Please define the class Pet. The class should include a constructor,
which takes the initial values of the attributes name, species and
year_of_birth as its arguments, in that specific order.

Please also write a function named new_pet(name: str, species: str,
year_of_birth: int) outside the class definition. The function should
create and return a new object of type Pet, as defined in the class Pet.

An example of how the function is used:

fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)

Sample output
Fluffy
dog
2017
"""


# Write your solution here:
class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name: str, species: str, year_of_birth: int):
    return Pet(name, species, year_of_birth)


if __name__ == "__main__":
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth)

"""
# Suggested solution

class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth
 
def new_pet(name: str, species: str, year_of_birth: int):
    pet = Pet(name, species, year_of_birth)
 
    return pet

#Review
My solution results in the same output, suggested one just uses an intermediate variable.
"""
