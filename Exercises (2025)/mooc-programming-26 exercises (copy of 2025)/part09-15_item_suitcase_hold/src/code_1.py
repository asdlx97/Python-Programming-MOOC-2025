# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        # self.__actual_weight = 0 #The exercise forbid me to use this one
        self.__items = []

    def __str__(self):
        actual_weight = sum(item.weight() for item in self.__items)
        # First time using a ternary operator inside an f-string :D
        return f"{len(self.__items)} {'item' if len(self.__items) == 1 else 'items'} ({actual_weight} kg)"

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        if not self.__items:
            return None

        highest_weight = 0
        heaviest = None

        for item in self.__items:
            if not heaviest or (item.weight() >= highest_weight):
                heaviest = item
                highest_weight = item.weight()

        return heaviest


class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__actual_weight = 0
        self.__suitcases = []

    def __str__(self):
        return f"{len(self.__suitcases)} {'suitcase' if len(self.__suitcases) == 1 else 'suitcases'}, space for {self.__max_weight - self.__actual_weight} kg"

    def add_suitcase(self, suitcase: Suitcase):
        if self.__actual_weight + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)
            self.__actual_weight += suitcase.weight()

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()


if __name__ == "__main__":

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
