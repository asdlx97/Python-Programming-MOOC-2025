# Write your solution here
from statistics import mean


def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = [person1, person2, person3]

    smallest = person1

    overall_mean = None

    for person in persons:
        results = [person["result1"], person["result2"], person["result3"]]
        personal_mean = mean(results)
        if overall_mean == None or personal_mean < overall_mean:
            overall_mean = personal_mean
            smallest = person

    return smallest


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
