"""
The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points	grade
< 0	impossible!
0-49	fail
50-59	1
60-69	2
70-79	3
80-89	4
90-100	5
> 100	impossible!

Some examples:

Sample output
How many points [0-100]: 37
Grade: fail

Sample output
How many points [0-100]: 76
Grade: 3

Sample output
How many points [0-100]: -3
Grade: impossible!

"""
# Write your solution here
points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
    print("Grade: impossible!")
elif points >= 0 and points <= 49:
    print("Grade: fail")
elif points <= 59:
    print("Grade: 1")
elif points <= 69:
    print("Grade: 2")
elif points <= 79:
    print("Grade: 3")
elif points <= 89:
    print("Grade: 4")
else:
    print("Grade: 5")

"""
# Suggested solution
points = int(input("How many points [0-100]: "))
 
if points < 0 or points > 100:
    grade = "impossible!"
elif points < 50:
    grade = "fail"
elif points < 60:
    grade = "1"
elif points < 70:
    grade = "2"
elif points < 80:
    grade = "3"
elif points < 90:
    grade = "4"
else:
    grade = "5"
 
print(f"Grade: {grade}")

#Review
My solution results in same output, but suggested one uses < comparisons for simplicity, 
and doesn't repeat the print statement inbetween each conditional statement which makes it cleaner.
"""