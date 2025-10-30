"""
Please write a program which asks the user for a positive integer number. 
The program then prints out a list of multiplication operations until 
both operands reach the number given by the user. See the examples below for details:

Sample output
Please type in a number: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4

Sample output
Please type in a number: 3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

"""
# Write your solution here
number = int(input("Please type in a number: "))
i = 1

while i <= number:
    if number < 0:
        break
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1

"""
# Suggested solution

number = int(input("Please type in a number: "))
counter1 = 1
while counter1 <= number:
    counter2 = 1
    while counter2 <= number:
        print(f"{counter1} x {counter2} = {counter1*counter2}")
        counter2 += 1
    counter1 += 1

#Review
Mostly same scripts, same outputs. My solution checks within loop if nuber isn't negative
but this doesn't seem necessary as the loop only runs if the counter is smaller than or equal
to the number, which is 1 to begin with.

#TODO Rewrite using the for loop once covered in course.
""" 