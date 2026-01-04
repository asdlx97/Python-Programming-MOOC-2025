"""
You have the CSV files from the previous exercise at your disposal
again. Please write a function named final_points(), which returns
the final exam points received by the students, in a dictionary format,
following these criteria:

If there are multiple submissions for the same task, the submission
with the highest number of points is taken into account.
If the submission was made over 3 hours after the start time, the submission is ignored.
The tasks are numbered 1 to 8, and each submission is graded with 0 to 6 points.

In the dictionary returned the key should be the name of the student,
and the value the total points received by the student.

Hint: nested dictionaries might be a good approach when processing
the tasks and submission times of each student.
"""

import csv
from datetime import datetime, timedelta


# Write your solution here
def store_students_tasks():
    students = []
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            students.append(
                {
                    "name": line[0],
                    "start": datetime.strptime(line[1], "%H:%M"),
                    "cheater": False,
                    "tasks": [],
                    "total_points": 0,
                }
            )

    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            student_name = line[0]
            task_no = line[1]
            task_points = line[2]
            task_end = datetime.strptime(line[3], "%H:%M")
            for student in students:
                if student_name == student["name"]:
                    task_duration = task_end - student["start"]
                    student["tasks"].append(
                        {
                            "no": task_no,
                            "points": task_points,
                            "end": task_end,
                            "duration": task_duration,
                        }
                    )

    return students


def final_points():
    students_tasks = store_students_tasks()

    points_per_student = {}

    for student in students_tasks:
        total_points = 0
        unique_tasks = {}
        for task in student["tasks"]:
            if task["no"] in unique_tasks.keys() or task["duration"] > timedelta(
                hours=3
            ):
                continue
            no = task["no"]
            best_score = task["points"]
            for other_task in student["tasks"]:
                if other_task["duration"] > timedelta(
                    hours=3
                ):  # This was my mistake not to check again, leading to add a task of over 3h to add to Tiina's points
                    continue
                if other_task["no"] == no and other_task["points"] > best_score:
                    best_score = other_task["points"]

            unique_tasks[no] = best_score

        if student["name"] == "tiina":
            print(unique_tasks)

        for point in unique_tasks.values():
            total_points += int(point)

        points_per_student[student["name"]] = total_points

    return points_per_student
    # Debugging Tiina
    # for student in students_tasks:
    #     if student["name"] == "tiina":
    #         sorted_tasks = sorted(student["tasks"], key=lambda task: task["no"])
    #         for task in sorted_tasks:
    #             if task["duration"] <= timedelta(hours=3):
    #                 print(task["no"], task["points"], task["duration"])


if __name__ == "__main__":
    final_points()

"""
# Suggested solution

import csv
from datetime import datetime, timedelta
 
def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student time and points is saved to a dictionary
        # Time and points is saved as tuple.
        points = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            tno = int(row[1])
            p = int(row[2])
            time = datetime.strptime(row[3], "%H:%M")
 
            # If cheating has happened, submission is not handled
            if time - start_times[name] > timedelta(hours=3):
                continue
 
            # If student is not handled yet, add student directly to the dictionary
            if name not in points:
                default_time = datetime(1900, 1, 1)
                points[name] = {}
                for i in range(1, 8+1):
                    points[name][i] = 0
                points[name][tno] = p
 
            # If student already exists, more points than earlier is required
            elif p > points[name][tno]:
                points[name][tno] = p
 
        final_points = {}
        # Iterate through students one by one
        for student in points:
            p = 0
            for exercise in points[student]:
                p += points[student][exercise]
            final_points[student] = p
 
        return final_points

#Review
My solution results in the same output. The suggested version is cleaner and computationally 
efficient, using a direct dictionary-based approach to store only what matters. It uses a nested 
dictionary directly mapping points[name][task_no] = points, updating only when higher points appear.
This avoids looping twice through the same student’s tasks, reducing time complexity.
"""
