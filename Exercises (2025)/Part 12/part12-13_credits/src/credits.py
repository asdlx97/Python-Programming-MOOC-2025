"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

In this exercise we will work with a slightly modified version of the CourseAttempt class. The name of the student is omitted, but the number of credits is included. The class works as follows:

attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
print(attempt)
print(attempt.course_name)
print(attempt.credits)
print(attempt.grade)

Sample output
Data Structures and Algorithms (10 cr) grade 3
Data Structures and Algorithms
10
3
The sum of all credits

Please implement a function named sum_of_all_credits which takes a list of course attempts as its argument. The function sums up the total number of study credits covered by the courses. It should work like this:

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_all_credits([s1, s2, s3])
print(credit_sum)
Sample output
20
Please implement the function using the reduce function.

The sum of passed credits

Please implement a function named sum_of_passed_credits which takes a list of course attempts as its argument. The function sums up the credits for the course attempts with grade 1 or above. It should work like this:

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_passed_credits([s1, s2, s3])
print(credit_sum)

Sample output
15
Please implement the function using the reduce and filter functions.

Average grade for passed courses

Please implement a function named average which takes a list of course attempts as its argument. The function calculates the average grade for the course attempts with grade 1 or above. It should work like this:

s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
ag = average([s1, s2, s3])
print(ag)

Sample output
4.0
Please implement the function using the reduce and filter functions. NB: the exercise asks for a simple mean value, not a weighted average.

While working on this exercise, it is likely worth remembering that the return value of filter is an iterator.
"""

from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda  sum, attempt:sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda  sum, attempt:sum + attempt.credits, filter(lambda c: c.grade > 1, attempts), 0)

def average(attempts: list):
    filtered = list(filter(lambda c: c.grade > 1, attempts))
    return reduce(lambda  sum, attempt:((sum*(len(filtered))) + attempt.grade)/len(filtered), filtered, 0)



if __name__ == "__main__":
    # #Part1: Sum of all credits
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_all_credits([s1, s2, s3])
    # print(credit_sum)

    # #Part 2: Sum of passed credits
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_passed_credits([s1, s2, s3])
    # print(credit_sum)

    #Part 3: Average grade for passed courses
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # ag = average([s1, s2, s3])
    # print(ag)

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Programming Course", 4, 5)
    s3 = CourseAttempt("Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)

"""
#Suggested solution

from functools import reduce
 
class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits
 
    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
 
def credit_summer(cr_sum, attempt):
    return cr_sum + attempt.credits
 
def sum_of_all_credits(attempts: list):
    return reduce(credit_summer, attempts, 0)
 
def sum_of_passed_credits(attempts: list):
    accepted = filter(lambda s: s.grade > 0, attempts)
    return reduce(credit_summer, accepted, 0)
 
def average(attempts: list):
    def grade_summer(cr_sum, attempt):
        return cr_sum + attempt.grade 
 
    accepted = list(filter(lambda s: s.grade > 0, attempts))
    sum_of_grades = reduce(grade_summer, accepted, 0)
 
    return sum_of_grades / len(accepted)
 
#Review
My solution results in the same output, the suggested one uses more helper
functions and calculates the mean after summing with reduce, while I do it within the reduce function.
"""