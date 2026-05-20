"""
This exercise will continue from the previous one. Now we shall print out some
statistics based on the CSV files.

Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3

Each row contains the information for a single student. The number of exercises
completed, the number of exercise points awarded, the number of exam points awarded,
 the total number of points awarded, and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.

You might find the f-strings covered in part 4 useful here.

F-strings differentiate between strings and numbers when it comes to justifying
columns:

word = "python"
print(f"{word:10}continues")
print(f"{word:>10}continues")

Sample output
python    continues
    pythoncontinues

As you can see above, by default strings are justified to the left edge of the
area specified for them. The > symbol can be used to justify to the right edge.

With number values the logic is reversed:

number = 42
print(f"{number:10}continues")
print(f"{number:<10}continues")

Sample output
        42continues
42        continues
With numbers the default behaviour is to justify to the right edge. The symbol
< can be used to justify to the left edge.

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

print(
    f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"
)

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
    print(
        f"{name:30}{total_exercises:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{final_grade:<10}"
    )

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
 
print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for eid, name in students.items():
    exec_nbr = exercises[eid]
    exec_score = to_points(exec_nbr)
    exam_points = exams[eid]
    total_points = exec_score + exam_points
    print(f"{name:30}{exec_nbr:<10}{exec_score:<10}{exam_points:<10}{total_points:<10}{grade(total_points):<10}")
 
    
#Review
My solution produces the same output, was easy to build onwards from the previous
exercise and a good way to practice print formatting!!
 """
