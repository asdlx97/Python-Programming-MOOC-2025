"""
Let's revisit the course grading project from the previous section.

As we left if last time, the program read and processed files containing student
information, completed exercises and exam results. We'll add a file containing
information about the course. An example of the format of the file:

Sample data

name: Introduction to Programming
study credits: 5
The program should then create two files. There should be a file called results.txt
with the following contents:

Sample data
Introduction to Programming, 5 credits
======================================
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3
The statistics section is identical to the results printed out in part 3 of the
project. The only addition here is the header section.

Additionally, there should be a file called results.csv with the following format:

Sample data
12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3
When the program is executed, it should look like this:

Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
Course information: course1.txt
Results written to files results.txt and results.csv
That is, the program only asks for the names of the input files. All output should
be written to the files. The user will only see a message confirming this.

NB: this exercise doesn't ask you to write any functions, so you should not place
any code within an if __name__ == "__main__" block.
"""

# tee ratkaisu tänne
# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    grades_data = input("Exam points: ")
    course_data = input("Course information: ")
else:
    # Hardcoded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    grades_data = "exam_points1.csv"
    course_data = "course1.txt"


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

# Reading and processing course information file
course_information = {}
with open(course_data) as new_file:
    for line in new_file:
        parts = line.split(":")
        course_information[parts[0].strip()] = parts[1].strip()

# Assembling the header
course_header = (
    f"{course_information['name']}, {course_information['study credits']} credits"
)
underlined_course_header = f"{course_header}\n{'='*len(course_header)}"

grading_table = [(0, 14, 0), (15, 17, 1), (18, 20, 2), (21, 23, 3), (24, 27, 4)]

# Assemble table header
table_header = f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"

# Assemble table contents
txt_table_contents = []
csv_table_contents = []
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

    txt_table_contents.append(
        f"{name:30}{total_exercises:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{final_grade:<10}"
    )
    csv_table_contents.append(f"{pic};{name};{final_grade}")

# Writing results to the txt file
with open("results.txt", "w") as my_file:
    my_file.write(underlined_course_header + "\n")
    my_file.write(table_header + "\n")

    for line in txt_table_contents:
        my_file.write(line + "\n")

# Writing results to the csv file
with open("results.csv", "w") as my_file:
    for line in csv_table_contents:
        my_file.write(line + "\n")


"""
# Suggested solution


student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
course_data = input("Course information: ")
 
def get_grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
    return a
 
def as_score(number):
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
 
with open(course_data) as file:
    rows = []
    for row in file:
        rows.append(row)
 
    course_name = rows[0][5:].strip()
    credits = int(rows[1][14:])
 
with open("results.txt", "w") as file:
    header = f"{course_name}, {credits} credits\n"
    file.write(header)
    separator = "="*(len(header)-1)
    file.write(f"{separator}\n")
    file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for student_id, name in students.items():
        exer = exercises[student_id]
        exer_score = as_score(exer)
        exam_pts = exams[student_id]
        tot_score = exer_score + exam_pts
        file.write(f"{name:30}{exer:<10}{exer_score:<10}{exam_pts:<10}{tot_score:<10}{get_grade(tot_score):<10}\n")
 
with open("results.csv", "w") as file:
    for student_id, name in students.items():
        exer = exercises[student_id]
        exer_score = as_score(exer)
        exam_pts = exams[student_id]
        tot_score = exer_score + exam_pts
        row = ";".join([student_id, name, str(get_grade(tot_score))])
        file.write(f"{row}\n")
 

#Review
My solution correctly processes all input files, calculates grades, and generates 
both the `results.txt` and `results.csv` files exactly as required. It efficiently
 uses dictionaries to organize data and dynamically formats the output. Unlike the 
 suggested solution, I didn’t use helper functions such as `get_grade` or `as_score`
because the exercise specifically stated that they weren’t expected, so I kept 
all logic within the main flow for consistency with the instructions. 
  
My approach to parsing the course information file by splitting on colons is more 
flexible than their fixed string slicing, but their version is cleaner and 
slightly more modular. Both solutions produce identical results, but mine 
focuses on precision and adherence to the given requirements, while the suggested
one emphasizes structure and reusability.
 """
