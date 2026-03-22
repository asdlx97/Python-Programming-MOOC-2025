"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

The exercise template contains the class definition for a CourseAttempt. It works like this:

attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
print(attempt.student_name)
print(attempt.course_name)
print(attempt.grade)
print(attempt)
Sample output
Peter Python
Introduction to Programming
5
Peter Python, grade for the course Introduction to Programming 5
Names of students

Please write a function named names_of_students(attempts: list) which takes a list of CourseAttempt objects as its argument. The function should return a new list with the names of the students who have attempted the course.

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in names_of_students([s1, s2, s3]):
    print(name)
Sample output
Peter Python
Olivia C. Objective
Peter Python
Please implement the function using the map function.

Courses

Please write a function named course_names(attempts: list) which takes a list of CourseAttempt objects as its argument. The function should return a new list containing the names of the courses on the original list in alphabetical order. Each course name should appear only once on the list.

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in course_names([s1, s2, s3]):
    print(name)
    
Sample output
Advanced Course in Programming
Introduction to Programming
Please implement the function using the map function. That alone will likely not be enough, however. You will need something else, too, to make sure the course names are unique.
"""


class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here
def names_of_students(attempts: list):
    return map(lambda s: s.student_name, attempts)

def course_names(attempts: list):
    return sorted(list(set(map(lambda c: c.course_name, attempts))))

if __name__ == "__main__":
    #Part 1: names of students
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in names_of_students([s1, s2, s3]):
        print(name)
    
    #Part 2: Courses
    for name in course_names([s1, s2, s3]):
        print(name)

"""
#Suggested solution

class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade
 
    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
 
def names_of_students(course_names: list):
    def student(attempt: CourseAttempt):
        return attempt.student_name
 
    return map(student, course_names)
    # same using lambda function
    # return map(lambda k: k.student_name, course_names)
 
def course_names(course_names: list):
    names = map(lambda k: k.course_name, course_names)
    # remove duplicates by using a set
    return sorted(list(set(names)))
 

#Review
My solution results in the same output, the suggested one uses the
choice() method from the random module while I use teh choices() method.
"""