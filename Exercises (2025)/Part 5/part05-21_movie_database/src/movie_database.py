"""
Please write a function named add_movie(database: list, name: str, director: str,
year: int, runtime: int), which adds a new movie object into a movie database.

The database is a list, and each movie object in the list is a dictionary.
The dictionary should contain the following keys.

name
director
year
runtime
The values attached to these keys are given as arguments to the function.

An example of its use:

database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)

Sample output
[{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017,
"runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin",
"year": 2001, "runtime": 94}]
"""


# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {}

    movie["name"] = name
    movie["director"] = director
    movie["year"] = year
    movie["runtime"] = runtime

    database.append(movie)


if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)

"""
# Suggested solution

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # Python accepts splitting rows from punctuation
    # The addition becomes more readable when parts are divided into separate rows
    movie = {"name": name,
               "director": director,
               "year": year,
               "runtime": runtime}
 
    database.append(movie)
    
#Review
My solution produces the same output as the suggested one. Structurally, 
the only difference is stylistic as I built the dictionary step by step, 
while the suggested version defines it inline using a single literal expression. 

Both are equally correct, but the suggested approach is more concise and readable, 
especially for short dictionaries like this.
"""
