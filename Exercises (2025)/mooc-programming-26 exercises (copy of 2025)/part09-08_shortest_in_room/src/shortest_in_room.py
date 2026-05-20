# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height})"


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if self.persons:
            return False
        else:
            return True
        # Could've been one line return len(self.persons) == 0 or return not self.persons

    def print_contents(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        # Could've been done in one line total_height = sum(p.height for p in self.persons)

        print(
            f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm"
        )
        for person in self.persons:
            print(person)

    def shortest(self):
        if not self.persons:
            return None

        shortest = self.persons[0]

        for person in self.persons:
            if person.height < shortest.height:
                shortest = person

        return shortest

    def remove_shortest(self):
        if not self.persons:
            return None

        shortest_person = self.shortest()

        self.persons.remove(shortest_person)

        return shortest_person


if __name__ == "__main__":
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
