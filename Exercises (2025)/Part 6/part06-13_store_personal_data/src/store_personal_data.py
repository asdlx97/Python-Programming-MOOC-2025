"""
Please write a function named store_personal_data(person: tuple),
which takes a tuple containing some identifying information as its argument.

The tuple contains the following elements:

Name (string)
Age (integer)
Height (float)

This should be processed and written into the file people.csv.
The file may already contain some data; the new entry goes to the end of the file.
The data should be written in the format

name;age;height

Each entry should be on a separate line. If we call the function with the argument
("Paul Paulson", 37, 175.5), the function should write this line to the end of the
file:

Paul Paulson;37;175.5
"""


# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as my_file:
        line = ""
        for value in person:
            line += f"{value};"
        line = line[:-1]
        my_file.write(line + "\n")


"""
# Suggested solution


def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        row = person[0] + ";"
        row += str(person[1]) + ";"
        row += str(person[2])

        file.write(row + "\n")
 

#Review
My solution results in the same output, only I use a loop which is more flexible if tuple ever changes.
 """
