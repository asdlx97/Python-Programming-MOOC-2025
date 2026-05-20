"""
This program calculates the end of year bonus a customer receives on their loyalty card. 
The bonus is calculated with the following formula:

If there are less than a hundred points on the card, the bonus is 10 %
In any other case the bonus is 15 %
The program should work like this:

Sample output
How many points are on your card? 55
Your bonus is 10 %
You now have 60.5 points

But there is a problem with the program, so with some inputs it doesn't work quite right:

Sample output
How many points are on your card? 95
Your bonus is 10 %
Your bonus is 15 %
You now have 120.175 points

Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.


# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")
"""
# Fix the program
points = int(input("How many points are on your card? "))
adjusted_points = 0

if points < 100:
    adjusted_points = points * 1.1
    print("Your bonus is 10 %")

if points >= 100:
    adjusted_points = points * 1.15
    print("Your bonus is 15 %")

print("You now have", adjusted_points, "points")

"""
#Suggested Solution

points = int(input("How many points are on your card? "))
if points < 100:
    factor = 1.1
    print("Your bonus is 10 %")
    
if points >= 100:
    factor = 1.15
    print("Your bonus is 15 %")
 
# a *= b is the same thing as a = a * b
points *= factor
print("You now have", points, "points")

#Review
Both my solution and the suggested one are using an extra variable, but in a different way, to make sure the 
added bonus calculation doesn't happen twice to the same points base. 

An easier solution would've been to use an if-else statement but we haven't seen that in the course
so I'll keep that one for later.
"""