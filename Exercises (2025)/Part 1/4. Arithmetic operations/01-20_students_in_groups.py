"""
Please write a program which asks for the number of students on a course and the desired group size. 
The program will then print out the number of groups formed from the students on the course. 
If the division is not even, one of the groups may have fewer members than specified.

If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. 
The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.

Sample output
How many students on the course? 8
Desired group size? 4
Number of groups formed: 2

Sample output
How many students on the course? 11
Desired group size? 3
Number of groups formed: 4

Hint: the integer division operator // could come in handy here.

"""
# Write your solution here
numberOfStudents = int(input("How many students on the course? "))
desiredGroupSize = int(input("Desired group size? "))

if numberOfStudents // desiredGroupSize < numberOfStudents / desiredGroupSize:
    print(f"Number of groups formed: {int((numberOfStudents // desiredGroupSize)) + 1}")

else:
    print(f"Number of groups formed: {(numberOfStudents // desiredGroupSize)}")

"""
#Suggested Solution

students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
 
groups = (students + group_size - 1) // group_size
 
print("Number of groups formed:", groups)
 
#Review
My solution results in the same output. The main difference is how the proposed solution 
only takes a line and makes better use of maths. I couldn't come up with that, but it seems that I
had a feeling a 1 should be added or substracted. Which I did inside my improvised if/else statement,
which I haven't learned yet but am eager to discover in the next chapter and come back if necessary.
"""

