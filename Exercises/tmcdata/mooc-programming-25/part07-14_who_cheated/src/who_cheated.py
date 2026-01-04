"""
The file start_times.csv contains individual start times for
a programming exam, in the format name;hh:mm. An example:

jarmo;09:00
timo;18:42
kalle;13:23
Additionally, the file submissions.csv contains points and
handin times for individual exercises. The format here is
name;task;points;hh:mm. An example:

jarmo;1;8;16:05
timo;2;10;21:22
jarmo;2;10;19:15
jne...
Your task is to find the students who spent over 3 hours on
the exam tasks. That is, any student whose any task was handed
in over 3 hours later than their exam start time is labelled
a cheater. There may be more than one submission for the same
task for each student. You may assume all times are within the same day.

Please write a function named cheaters(), which returns a list
containing the names of the students who cheated
"""

# Write your solution here
import csv
from datetime import datetime, timedelta


def cheaters():
    students = []
    cheaters = []
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            students.append(
                {
                    "name": line[0],
                    "start": datetime.strptime(line[1], "%H:%M"),
                    "cheater": False,
                    "tasks": [],
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

                    if task_duration > timedelta(hours=3):
                        student["cheater"] = True
                        if student["name"] not in cheaters:
                            cheaters.append(student["name"])

    return cheaters


"""
# Suggested solution

import csv
from datetime import datetime, timedelta
 
def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
            # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time
        
        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
 
        return cheaters

#Review
My solution results in the same output. The suggested version is more concise and 
efficient, focusing on the key logic — comparing the last submission time to the start time — 
without extra data storage. But I wanted the data to be in place for future exercises... (next one)
"""
