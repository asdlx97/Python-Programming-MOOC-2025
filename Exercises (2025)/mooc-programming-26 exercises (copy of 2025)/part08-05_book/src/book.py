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
