"""
This program works with two CSV files.
One of them contains information about some students on a course:

id;first;last
12345678;peter;pythons
12345687;jean;javanese
12345699;alice;adder

The other contains the number of exercises each student has completed each week:

id;e1;e2;e3;e4;e5;e6;e7
12345678;4;1;1;4;5;2;4
12345687;3;5;3;1;5;4;6
12345699;10;2;2;7;10;2;2

As you can see above, both CSV files also have a header row, which tells you what
each column contains.

Please write a program which asks the user for the names of these two files, reads
the files, and then prints out the total number of exercises completed by each
student. If the files have the contents in the examples above, the program should
print out the following:

Sample output
Student information: students1.csv
Exercises completed: exercises1.csv
pekka peloton 21
jaana javanainen 27
liisa virtanen 35
Hint: while testing your program, you may quickly run out of patience if you always
have to type in the file names at the prompt. You might want to hard-code the user
input, like so:

if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
The actual functionality of the program is now "hidden" in the False branch of an if
 statement. It will never be executed.

Now, if you want to quickly verify the program works correctly also with user input,
 you can just replace False with True:


if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
When you have verified your program works correctly, you can remove the if structure,
 keeping the commands asking for input.

NB: this exercise doesn't ask you to write any functions, so you should not place
any code within an if __name__ == "__main__" block.

NB2: If Visual Studio can't find the file and you have checked that there are no
spelling errors, take a look at these instructions.
"""

# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # Hardcoded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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

# # Printing file names
# print(f"Student information: {student_info}")
# print(f"Exercises completed: {exercise_data}")

# Printing total amount of exercises per student
for pic, name in students.items():
    if pic in exercises:
        total_exercises = sum(exercises[pic])
        print(f"{name} {total_exercises}")

"""
# Suggested solution

student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
 
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
 
for student_id, name in students.items():
    print(f"{name} {exercises[student_id]}")
    
#Review
My solution produces the same output as the suggested one. 
Structurally, though, I stored each student’s weekly exercises in a list and 
summed them later, whereas the suggested version calculates the total 
immediately while reading each row. 

Their approach is more memory-efficient and simpler, since only the sum is needed
but I assume I'll need that list in one of the next exercises??
 """
