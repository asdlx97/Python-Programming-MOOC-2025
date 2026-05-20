"""
The file solutions.csv contains some solutions to mathematics problems:

Arto;2+5;7
Pekka;3-2;1
Erkki;9+3;11
Arto;8-3;4
Pekka;5+5;10
...jne...

As you can see above, on each line the format is name_of_student;problem;result.
All the operations are either addition or subtraction, and each has exactly two
operands.

Please write a function named filter_solutions() which

Reads the contents of the file solutions.csv
writes those lines which have a correct result into the file correct.csv
writes those lines which have an incorrect result into the file incorrect.csv
Using the example above, the file correct.csv would contain the lines

Arto;2+5;7
Pekka;3-2;1
Pekka;5+5;10
The other two would be in the file incorrect.csv.

Please write the lines in the same order as they appear in the original file.
Do not change the original file.

NB: the function should have the exact same result, no matter how many times it is
called. That is, it shouldn't matter if the function is called once

filter_solutions()
or multiple times in a row

filter_solutions()
filter_solutions()
filter_solutions()
filter_solutions()

After the execution, the contents of the files correct.csv and incorrect.csv
should be exactly the same in either case.
"""


# Write your solution here
def filter_solutions():
    # Read and stor contents of solutions.csv
    correct = []
    incorrect = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            parts = line.strip().split(";")

            name = parts[0]
            problem = parts[1]
            result = parts[2]

            # Splitting per separator and storing it
            if "-" in problem:
                problem = problem.split("-")
                if int(problem[0]) - int(problem[1]) == int(result):
                    correct.append(f"{name};{problem[0]}-{problem[1]};{result}")
                else:
                    incorrect.append(f"{name};{problem[0]}-{problem[1]};{result}")

            elif "+" in problem:
                problem = problem.split("+")
                if int(problem[0]) + int(problem[1]) == int(result):
                    correct.append(f"{name};{problem[0]}+{problem[1]};{result}")
                else:
                    incorrect.append(f"{name};{problem[0]}+{problem[1]};{result}")

    open("correct.csv", "w").close()
    with open("correct.csv", "a") as new_file:
        for solution in correct:
            new_file.write(solution + "\n")

    open("incorrect.csv", "w").close()
    with open("incorrect.csv", "a") as new_file:
        for solution in incorrect:
            new_file.write(solution + "\n")


"""
# Suggested solution

def filter_solutions():
    # Open all lines
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")
 
            calculation = pieces[1]
            result = pieces[2]
 
            # Addition or subtraction?
            if "+" in calculation:
                operands = calculation.split("+")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) - int(operands[1]) == int(result)
 
            # Write to file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)
 

#Review
My solution produces the correct results and keeps file outputs consistent across 
multiple runs. It correctly separates valid and invalid solutions while maintaining order.

Structurally, the suggested version is more elegant as it uses multiple with 
statements to handle all files simultaneously, avoiding manual closing and 
clearing steps. It also writes directly to the appropriate file as it processes 
each line, making it more memory-efficient and concise.
 """
