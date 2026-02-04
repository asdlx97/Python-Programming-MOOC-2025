"""
Please write a class named Book with the attributes name, author, genre and year, along with a constructor which assigns initial values to these attributes.

Your class should work like this:

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")

Sample output
Luciano Ramalho: Fluent Python (2015)
The genre of the book High Adventure is autobiography

"""


# Write your solution here
class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries


class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


"""
# Suggested solution

class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries
 
class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount
 
class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional

#Review
My solution results in the same output, is same script too.
"""
