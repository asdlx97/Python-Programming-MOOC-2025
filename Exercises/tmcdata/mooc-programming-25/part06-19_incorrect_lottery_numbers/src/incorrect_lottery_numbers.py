"""
The file lottery_numbers.csv containts winning lottery
numbers in the following format:

Sample data
week 1;5,7,11,13,23,24,30
week 2;9,13,14,24,34,35,37
...etc...
Each line should contain a header week x, followed
by seven integer numbers which are all between 1
and 39 inclusive.

The file has been corrupted. Lines in the file may
contain the following kinds of errors (these exact
lines may not be present in the file, but errors
in a similar format will be):

The week number is incorrect:

Sample data
week zzc;1,5,13,22,24,25,26
One or more numbers are not correct:

Sample data
week 22;1,**,5,6,13,2b,34
Too few numbers:

Sample data
week 13;4,6,17,19,24,33
The numbers are too small or large:

Sample data
week 39;5,9,15,35,39,41,105
The same number appears twice:

Sample data
week 41;5,12,3,35,12,14,36
Please write a function named filter_incorrect(),
which creates a file called correct_numbers.csv.
The file should contain only those lines from the
original file which are in the correct format.
"""


# Write your solution here
def filter_incorrect():
    correct_lines = []
    test = "Week 1;17,19,35,23,8,20,36"
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            line = line.strip()
            correct_line = True
            parts = line.split(";")

            # Check if week no is nr
            try:
                week_no = int(parts[0].split(" ")[1])
            except ValueError:
                continue

            winning_nos = parts[1].split(",")
            # Check for same nr appearing twice
            if len(winning_nos) != len(set(winning_nos)):
                continue
            # Check if they're all nrs
            # winning_nos_check = []
            try:
                for no in winning_nos:
                    if int(no) < 1 or int(no) > 39:
                        correct_line = False
                        break
            except ValueError:
                continue
            if len(winning_nos) < 7:
                continue

            if correct_line:
                winning_nos_str = ",".join(winning_nos)

                correct_lines.append(f"week {week_no};{winning_nos_str}")

    with open("correct_numbers.csv", "w") as new_file:
        for line in correct_lines:
            print(line)
            new_file.write(line + "\n")


if __name__ == "__main__":
    filter_incorrect()

"""
# Suggested solution

def filter_incorrect():
    with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
        for row in input_file:
            parts = row.strip().split(";")
            if len(parts) != 2:
                continue
            week = parts[0].split(" ")
            error = False
            if len(week) != 2 or week[0] != "week":
                error = True
            try:
                mika = int(week[1])
            except:
                error = True
            number_list = parts[1].split(",")
            if len(number_list) != 7:
                error = True
 
            # numbers already listed --> to find out duplicates
            listed = []
            for item in number_list:
                try:
                    number = int(item)
                    if number < 1 or number > 39 or number in listed:
                        error = True
                    listed.append(number)
                except:
                    error = True
            if not error:
                result_file.write(row)
 
#Review
My solution returns the same output, suggested one checks for more possible errors.
 """
