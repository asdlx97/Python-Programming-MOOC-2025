"""
Please write a program for recording the amount of time the user has
spent in front of a television, computer or mobile device screen over
a specific period of time.

The program should work as follows:

Sample output
Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
Please type in screen time in minutes on each day (TV computer mobile):
Screen time 24.06.2020: 60 120 0
Screen time 25.06.2020: 0 0 0
Screen time 26.06.2020: 180 0 0
Screen time 27.06.2020: 25 240 15
Screen time 28.06.2020: 45 90 5
Data stored in file late_june.txt
The user will input each day on a separate line, and the entries will
contain three numbers separated by spaces, representing minutes.

With the above input, the program should store the data in a file
named late_june.txt. The contents should look like this:

Sample data
Time period: 24.06.2020-28.06.2020
Total minutes: 780
Average minutes: 156.0
24.06.2020: 60/120/0
25.06.2020: 0/0/0
26.06.2020: 180/0/0
27.06.2020: 25/240/15
28.06.2020: 45/90/5
"""

# Write your solution here
from datetime import datetime, timedelta

time_period = ""
total_minutes = 0
average_minutes = 0.0
days_details = []

filename = input("Filename: ")
starting_date_input = input("Starting date: ")
starting_date = datetime.strptime(starting_date_input, "%d.%m.%Y")
amount_days = int(input("How many days: "))
end_date = starting_date + timedelta(days=amount_days - 1)

print("Please type in screen time in minutes on each day (TV computer mobile):")

i = starting_date
while i <= end_date:
    this_date = i.strftime("%d.%m.%Y")
    this_day_time_input = input(f"Screen time {this_date}: ")
    this_day_time = this_day_time_input.split(" ")

    for time in this_day_time:
        total_minutes += int(time)

    days_details.append(
        f"{this_date}: {this_day_time[0]}/{this_day_time[1]}/{this_day_time[2]}"
    )

    i += timedelta(days=1)

time_period = f"{starting_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}"
average_minutes = total_minutes / amount_days

with open(filename, "w") as new_file:
    new_file.write(f"Time period: {time_period}\n")
    new_file.write(f"Total minutes: {str(total_minutes)}\n")
    new_file.write(f"Average minutes: {str(average_minutes)}\n")

    for day in days_details:
        new_file.write(f"{day}\n")

print(f"Data stored in file {filename}")

"""
# Suggested solution

from datetime import datetime, timedelta
 
week = timedelta(days=7)
 
def format(aika):
    return aika.strftime("%d.%m.%Y")
 
file = input("Filename: ")
start = input("Starting date: ").split('.')
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
screen_times = []
total = 0
start = datetime(int(start[2]), int(start[1]), int(start[0]))
 
for i in range(days):
    day = start + timedelta(days=i)
    times = input(f"Screen time {format(day)}: ").split(' ')
    tv = int(times[0])
    pc = int(times[1])
    mobile = int(times[2])
    total += tv + pc + mobile
    screen_times.append((day, tv, pc, mobile) )
 
with open(file, "w") as tdsto:
    tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    tdsto.write(f"Total minutes: {total}\n")
    tdsto.write(f"Average minutes: {total/days:.1f}\n")
    for pv, tv, pc, mob in screen_times:
        tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
 
print(f"Data stored in file {file}")

#Review
My solution results in the same output. The suggested solution however adds a
helper function to format the dates, stores each days details in tuples while
I pre-write the lines and append them to the list.
"""
