"""
Please write a phone book application. It should work as follows:

Sample output
command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...

As you can see above, each name can be attached to a single number only.
If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

NB: this exercise doesn't ask you to write any functions, so you should not place any
code within an if __name__ == "__main__" block.
"""

# Write your solution here
phone_book = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1:
        name = input("name: ")

        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")

    if command == 2:
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")

    if command == 3:
        print("quitting...")
        break

"""
# Suggested solution

def search(persons):
    name = input("name: ")
    if name in persons:
        print(persons[name])
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()

#Review
My solution works correctly and produces the same output. 
Structurally, though, the suggested one is more modular and scalable as 
it separates the logic for searching, adding, and running the main loop 
into dedicated functions. This makes the code easier to maintain, extend, and test.
"""
