"""
Let's have a look at a JSON file, which contains some information about
students in the following format:

[
    {
        "name": "Peter Pythons",
        "age": 27,
        "hobbies": [
            "coding",
            "knitting"
        ]
    },
    {
        "name": "Jean Javanese",
        "age": 24,
        "hobbies": [
            "coding",
            "rock climbing",
            "reading"
        ]
    }
]
Please write a function named print_persons(filename: str), which reads
a JSON file in the above format, and prints the contents as shown below.
The file may contain any number of entries.

Sample output
Peter Pythons 27 years (coding, knitting)
Jean Javanese 24 years (coding, rock climbing, reading)
The hobbies should be listed in the same order as they appear in the JSON file.
"""

# Write your solution here
import json


def print_persons(filename: str):
    with open(filename) as new_file:
        content = new_file.read()

    persons = json.loads(content)

    for person in persons:
        hobbies = ""
        for hobby in person["hobbies"]:
            hobbies += f"{hobby}, "
        hobbies = hobbies.strip(", ")

        print(f"{person['name']} {person['age']} years ({hobbies})")


if __name__ == "__main__":
    print_persons("file1.json")

"""
# Suggested solution

import json
def print_persons(filename: str):
    with open(filename) as f:
        content = f.read()
    persons = json.loads(content)
    for person in persons:
        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        print(f"{name} {age} years ({hobbies})")

#Review
My solution results in the same output. The suggested solution however uses 
the join() function to concatenate the strings, which is cleaner.
"""
