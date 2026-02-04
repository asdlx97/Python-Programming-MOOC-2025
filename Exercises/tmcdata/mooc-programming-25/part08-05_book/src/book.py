"""
Please write a class named Book with the attributes name, author, genre and year,
along with a constructor which assigns initial values to these attributes.

Your class should work like this:

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")

Sample output
Luciano Ramalho: Fluent Python (2015)
The genre of the book High Adventure is autobiography
"""


# Write your solution here:
class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


if __name__ == "__main__":
    book1 = Book("Design Your Life", "Some MIT Authors", "Philosophy", 2015)
    book2 = Book("Myth of normal", "Gbor Mattéée", "Psychology", 2021)

    print(f"{book1.author}: {book1.name} ({book1.year})")
    print(f"The genre of the book {book2.name} is {book2.genre}")

"""
# Suggested solution

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

#Review
My solution results in the same output, follows same script.
"""
