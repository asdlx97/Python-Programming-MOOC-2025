"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately.
 You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to
 the button for executing tests .

In this series of exercises you will create a simple student database. Before diving in, please spend
a moment reading through the instructions and thinking about what sort of data structures are necessary
for organising the data stored by your program.

adding students

First write a function named add_student, which adds a new student to the database. Also write a
preliminary version of the function print_student, which prints out the information of a single student.

These function are used as follows:

students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")
Your program should now print out

Sample output
Peter:
 no completed courses
Eliza:
 no completed courses
Jack: no such person in the database
adding completed courses

Please write a function named add_course, which adds a completed course to the information of a
 specific student in the database. The course data is a tuple consisting of the name of the course
 and the grade:

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
print_student(students, "Peter")
When some courses have been added, the information printed out changes:

Sample output
Peter:
 2 completed courses:
  Introduction to Programming 3
  Advanced Course in Programming 2
 average grade 2.5
repeating courses

Courses with grade 0 should be ignored when adding course information. Additionally, if the
course is already in the database in that specific student's information, the grade recorded
in the database should never be lowered if the course is repeated.

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")

Sample output
Peter:
 2 completed courses:
  Introduction to Programming 3
  Advanced Course in Programming 2
 average grade 2.5
summary of database

Please write a function named summary, which prints out a summary based on all the
information stored in the database.

students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
add_course(students, "Peter", ("Data Structures and Algorithms", 1))
add_course(students, "Peter", ("Introduction to Programming", 1))
add_course(students, "Peter", ("Advanced Course in Programming", 1))
add_course(students, "Eliza", ("Introduction to Programming", 5))
add_course(students, "Eliza", ("Introduction to Computer Science", 4))
summary(students)
This should print out

Sample output
students 2
most courses completed 3 Peter
best average grade 4.5 Eliza
"""


# Write your solution here
def add_student(database: list, name: str):
    database[name] = []


def print_student(database: list, name: str):
    if name in database:
        if len(database[name]) == 0:
            print(f"{name}:\n no completed courses")
        else:
            print(f"{name}:")
            print(f" {len(database[name])} completed courses:")
            sum = 0
            for course in database[name]:
                print(f"  {course[0]} {course[1]}")
                sum += course[1]
            print(f" average grade {sum/len(database[name])}")
    elif name not in database:
        print(f"{name}: no such person in the database")


def add_course(database: list, name: str, course: tuple):
    if course[1] == 0:
        return
    if len(database[name]) == 0:
        database[name].append(course)
    else:
        for existing_course in database[name]:
            if existing_course[0] == course[0]:
                if existing_course[1] >= course[1]:
                    # course[1] = existing_course[1] #Error, tuple doesn't support assignment
                    break
                else:
                    database[name].remove(existing_course)
                    database[name].append(course)
            else:
                database[name].append(course)


def summary(database: list):

    most_courses = ("Peter", 0)
    for student in database:
        single_courses = []
        for course in database[student]:
            if course not in single_courses:
                single_courses.append(course)
        if len(single_courses) >= most_courses[1]:
            most_courses = (student, len(single_courses))

    best_average = ("Eliza", 0)
    for student in database:
        sum = 0
        for course in database[student]:
            sum += course[1]
        student_average = sum / len(database[student])
        if student_average >= best_average[1]:
            best_average = (student, student_average)

    print(f"students {len(database)}")
    print(f"most courses completed {most_courses[1]} {most_courses[0]}")
    print(f"best average grade {best_average[1]} {best_average[0]}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)

"""
# Suggested solution

def add_student(students: dict, name: str):
    students[name] = {}
 
def print_student(students: dict, name: str):
    if not name in students:
        print(f"{name}: no such person in the database")
        return
 
    students_completed_courses = students[name]
 
    print(f"{name}:")
    if len(students_completed_courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(students_completed_courses):} completed courses:")
        sum = 0
        for course, grade in students_completed_courses.items():
            course_grade = grade[1]
            print(f"  {course} {course_grade}")
            sum += course_grade
 
        print(f" average grade {sum/len(students_completed_courses):.1f}")
 
def add_course(students: dict, name: str, completion: tuple):
    students_completed_courses = students[name]
    course_name = completion[0]
    course_grade = completion[1]
 
    # failed course is not recorded in the database
    if course_grade==0:
        return
 
    # if previous grade is higher, new grade is not recorded in the database
    if course_name in students_completed_courses:
        if students_completed_courses[course_name][1] > course_grade:
            return
 
    students_completed_courses[course_name] = completion
 
def summary(students: dict):
    print(f"students {len(students)}")
    most_courses_count = 0
    best_avg_grade = 0
    for name, completions in students.items():
        if len(completions) > most_courses_count:
            most_courses = name
            most_courses_count = len(students[most_courses])
 
        sum = 0
        for course, grade in completions.items():
            sum += grade[1]
 
        if len(completions)==0:
            avg = 0
        else:
            avg = sum/len(completions)
 
        if avg>best_avg_grade:
            best_avg_grade = avg
            best = name
 
    print(f"most courses completed {most_courses_count} {most_courses}")
    print(f"best average grade {best_avg_grade:.1f} {best}")
    
#Review
My solution produces the correct outputs, but structurally it differs quite a bit from the suggested one. 
I used lists of tuples for storing course data, while the suggested solution uses nested dictionaries 
by mapping course names directly to tuples. That structure makes data access, updates, and overwriting 
much cleaner.
In my version, checking for existing courses and preventing duplicates requires looping through lists, 
which is more error-prone and less efficient. The suggested design simplifies those checks by leveraging 
dictionary keys, making grade comparisons and updates straightforward.
 """
