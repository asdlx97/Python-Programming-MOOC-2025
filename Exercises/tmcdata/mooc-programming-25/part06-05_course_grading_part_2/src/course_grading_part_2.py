"""
Let's expand the program created in the previous exercise. Now also the exam points
awarded to each student are contained in a CSV file. The contents of the file follow
 this format:

id;e1;e2;e3
12345678;4;1;4
12345687;3;5;3
12345699;10;2;2

In the above example the student whose student number is 12345678 was awarded 4+1+4
points in the exam, which equals a total of 9 points.

The program should again ask the user for the names of the files. Then the program
should process the files and print out a grade for each student.

Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
pekka peloton 0
jaana javanainen 1
liisa virtanen 3

Each completed exercise is counted towards exercise points, so that completing at
least 10 % of the total exercices awards 1 point, completing at least 20 % awards
2 points, etc. Completing all 40 exercises awards 10 points. The number of points
awarded is always an integer number.

The final grade for the course is determined based on the sum of exam and exercise
points according to the following table:

exam points + exercise points	grade
0-14	0 (fail)
15-17	1
18-20	2
21-23	3
24-27	4
28-	5

NB: this exercise doesn't ask you to write any functions, so you should not place
any code within an if __name__ == "__main__" block.
"""

# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    grades_data = input("Exam points: ")
else:
    # Hardcoded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    grades_data = "exam_points1.csv"

students = {}
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        pic = parts[0].strip()
        name = parts[1].strip() + " " + parts[2].strip()
        students[pic] = name

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        pic = parts[0].strip()
        exercises[pic] = []
        for week in parts[1:]:
            exercises[pic].append(int(week))

grades = {}
with open(grades_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        pic = parts[0].strip()
        grades[pic] = []
        for week in parts[1:]:
            grades[pic].append(int(week))

grading_table = [(0, 14, 0), (15, 17, 1), (18, 20, 2), (21, 23, 3), (24, 27, 4)]

for pic, name in students.items():
    if pic in exercises:
        total_exercises = sum(exercises[pic])
        exercise_points = int((total_exercises / 40) * 10)
    if pic in grades:
        exam_points = sum(grades[pic])
    total_points = exercise_points + exam_points
    if total_points >= 28:
        final_grade = 5
    else:
        for graderange in grading_table:
            if total_points in range(graderange[0], graderange[1] + 1):
                final_grade = graderange[2]
    print(f"{name} {final_grade}")

"""
# Suggested solution

student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
 
def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
 
    return a
 
def to_points(number):
    return number // 4
 
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum
 
exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        esum = 0
        for i in range(1, 4):
            esum += int(parts[i])
        exams[parts[0]] = esum
 
for student_id, name in students.items():
    total = exams[student_id] + to_points(exercises[student_id])
    print(f"{name} {grade(total)}")
    
#Review
My solution produces the same output, altough the exercie brief suggested not to
write any functions, the suggested solution put grading and point conversion 
into dedicated helper functions (grade() and to_points(). Its also uses a 
simpler threshold list (limits = [15, 18, 21, 24, 28]).

I agree that the model solution is more modular this way and easier to maintain,
and thought about writing helper functions but didn't as briefed.
 """
