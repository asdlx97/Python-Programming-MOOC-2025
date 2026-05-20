"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

The exercise template contains the class definition for a ClimbingRoute. It works as follows:

route1 = ClimbingRoute("Edge", 38, "6A+")
route2 = ClimbingRoute("Smooth operator", 11, "7A")
route3 = ClimbingRoute("Synchro", 14, "8C+")


print(route1)
print(route2)
print(route3.name, route3.length, route3.grade)

Sample output
Edge, length 38 metres, grade 6A+
Smooth operator, length 11 metres, grade 7A
Synchro 14 8C+
Sort by length

Please write a function named sort_by_length(routes: list) which returns a new list of routes, sorted by length from longest to shortest.

The function should work as follows:

r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]

for route in sort_by_length(routes):
    print(route)

Sample output
Edge, length 38 metres, grade 6A+
Synchro, length 14 metres, grade 8C+
Small steps, length 12 metres, grade 6A+
Smooth operator, length 11 metres, grade 7A
Sort by difficulty

Please write a function named sort_by_difficulty(routes: list) which returns a new list of routes, sorted by difficulty, i.e. grade, from hardest to easiest. For routes with the same grade, the longer one is more difficult. The scale of climbing route grades is 4, 4+, 5, 5+, 6A, 6A+, ..., which in practice works out as the alphabetical order for strings.

The function should work as follows:

r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]
for route in sort_by_difficulty(routes):
    print(route)
Sample output
Synchro, length 14 metres, grade 8C+
Smooth operator, length 11 metres, grade 7A
Edge, length 38 metres, grade 6A+
Small steps, length 12 metres, grade 6A+
Hint: if the order is based on a list or a tuple, by default Python sorts the items first based on the first item, next based on the second item, and so forth:

my_list = [("a", 4),("a", 2),("b", 30), ("b", 0) ]
print(sorted(my_list))

Sample output
[('a', 2), ('a', 4), ('b', 0), ('b', 30)]
"""


class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(routes: list):
    #Helper function
    def by_length(item: ClimbingRoute):
        return item.length

    return sorted(routes, key=by_length, reverse=True)

def sort_by_difficulty(routes: list):
    #Helper function
    def by_difficulty_length(item: ClimbingRoute):
        return (item.grade, item.length) #As python by default sorts tuple starting with first item, was a hint in the course.
    
    return sorted(routes, key=by_difficulty_length, reverse=True)

if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]

    for route in sort_by_length(routes):
        print(route)

    for route in sort_by_difficulty(routes):
        print(route)
        
"""
#Suggested solution

class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade
 
    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"
 
def sort_by_length(routes: list):
    def length_order(route):
        return route.length
 
    return sorted(routes, key=length_order, reverse=True)
 
def sort_by_difficulty(routes: list):
    def difficulty_order(route):
        return (route.grade, route.length)
 
    return sorted(routes, key=difficulty_order, reverse=True)

#Review
My solution results in the same output, the suggested one is the same script.
"""