"""
In this exercise you will create a small expansion to the phone book application. The code from the above example is in the exercise template. Please add a command which lets the user search the phone book by number. After the addition the application should work as follows:

Sample output
commands:
0 exit
1 add entry
2 search
3 search by number

command: 1
name: Eric
number: 02-123456

command: 1
name: Eric
number: 045-4356713

command: 3
number: 02-123456
Eric

command: 3
number: 0100100
unknown number

command: 0
Please implement this addition with respect to the current structure of the program. This means that in the PhoneBookApplication class you should add an appropriate helper method to allow for the new functionality, and also add a new branch to the while loop. In the PhoneBook class you should add a method which allows for searching with a number.

NB: as you test your program and end up with lots of different numbers stored in the phonebook.txt file, there is a chance the local tests will not be passed if conflicting data is read from the file as the app starts. You can try emptying the contents of any phonebook.txt files you find in the directory for the exercise before running the local tests. Which one of the files is used by your program may depend on your Visual Studio Code settings. Please have a look at the explanation in part 6. If your solution is correct, the tests on the server should still pass normally, regardless.
"""

# WRITE YOUR SOLUTION HERE:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def get_names(self, number: str):
        found =  False
        for name, nrs in self.__persons.items():
            if number in nrs:
                found = True
                return name
        if not found:
            return None
        else:
            return name

    def all_entries(self):
        return self.__persons

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers
        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")
                
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search_by_name(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def search_by_number(self):
        number = input("number: ")
        names = self.__phonebook.get_names(number)
        if names == None:
            print("unknown number")
            return 
        print(names)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search_by_name()
            elif command == "3":
                self.search_by_number()
            else:
                self.help()

# when you run the tests, nothing apart from these two lines should be placed in the main function, outside any class definitions 
application = PhoneBookApplication()
application.execute()

"""
#Suggested Solution 

# WRITE YOUR SOLUTION HERE:
class PhoneBook:
    def __init__(self):
        self.__persons = {}
 
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []
 
        self.__persons[name].append(number)
 
    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
 
    def search_with_number(self, number: str):
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name
 
        return None
 
    def all_entries(self):
        return self.__persons
 
class FileHandler():
    def __init__(self, filename):
        self.__filename = filename
 
    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers
        return names
 
    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")
                
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")
 
        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)
 
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")
 
    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
 
    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)
 
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())
 
    def search_by_number(self):
        number = input("number: ")
        name = self.__phonebook.search_with_number(number)
        if name == None:
            print("unknown number")
        else:
            print(name)
 
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_by_number()
            else:
                self.help()
 
# when you run the tests, nothing apart from these two lines should be placed in the main function, outside any class definitions 
application = PhoneBookApplication()
application.execute()
 

#Review
My solution produces the same output and follows the same overall program structure as the suggested solution.
To implement the new functionality, I added a method to the PhoneBook class which searches for a name based on a given phone number. This method iterates through the stored dictionary of persons and their number lists, returning the matching name if the number is found, or None otherwise.
In the PhoneBookApplication class I added a new helper method search_by_number, which asks the user for a number, calls the corresponding PhoneBook method, and prints either the found name or "unknown number" if no match exists. I also added a new branch to the command loop so the program executes this helper method when the user enters command 3.

One difference from the suggested solution is that my method in PhoneBook is named get_names instead of search_with_number, and I included an additional boolean flag to track whether a match was found. Functionally this behaves the same, although the suggested solution simplifies the logic by returning immediately when a match is found.
Overall the structure of the program remains the same and the added functionality integrates correctly with the existing classes, producing the expected behaviour for searching the phone book by number.
"""