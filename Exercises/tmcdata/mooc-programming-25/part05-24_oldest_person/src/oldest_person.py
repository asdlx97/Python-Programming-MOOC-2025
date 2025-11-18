"""
Please write a function named oldest_person(people: list), which takes a list of tuples
as its argument. In each tuple, the first element is the name of a person, and the
second element is their year of birth. The function should find the oldest person on
the list and return their name.

An example of the function in action:

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))

Sample output
Mary
"""


# Write your solution here
def oldest_person(people: list):
    year = 2025
    oldest = ""
    for person in people:
        if person[1] < year:
            year = person[1]
            oldest = person[0]

    return oldest


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))

"""
# Suggested solution

def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        # comparing the year of birth of the oldest known person and the person in turn
        if person[1] < oldest[1]:
            oldest = person
 
    return oldest[0]
    
#Review
My solution produces the same correct result. Structurally, the suggested one is more 
elegant as it initializes oldest with the first person tuple instead of using arbitrary 
placeholder values. 

This makes the code more general and avoids hardcoding a reference year.
Both correctly compare birth years to find the earliest, but the suggested version is 
cleaner and slightly more Pythonic by working directly with tuple data rather than 
separate variables.
 """
