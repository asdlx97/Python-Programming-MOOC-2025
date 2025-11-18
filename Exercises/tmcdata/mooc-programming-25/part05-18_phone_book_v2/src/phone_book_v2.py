"""
Please write an improved version of the phone book application.
Each entry should now accommodate multiple phone numbers.
The application should work otherwise exactly as above,
but this time all numbers attached to a name should be printed.

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
040-5466745
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...
"""


# Write your solution here
def search(persons):
    name = input("name: ")
    if name in persons:
        for number in persons[name]:
            print(number)
    else:
        print("no number")


def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = []
    persons[name].append(number)
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

"""
# Suggested solution

def search(persons):
    name = input("name: ")
    if name in persons:
        for number in persons[name]:
            print(number)
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = []
    persons[name].append(number)
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
Same output, same script. I built on the model solution from the previous exercise as it was more structured.
"""
