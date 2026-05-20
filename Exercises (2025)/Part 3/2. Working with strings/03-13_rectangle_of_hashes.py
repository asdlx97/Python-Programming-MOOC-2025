"""
Please modify the previous program so that it also asks for the height, 
and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
##########

"""
# Write your solution here
measure = "#"
width = int(input("Width: "))
height = int(input("Height: "))

while height > 0:
    print(measure*width)
    height -= 1

#print(("#" * width + "\n") * height) This would be a very simple oneliner

"""
# Suggested solution

width = int(input("Width: "))
height = int(input("Height: "))
 
n = 0
while n < height:
    print("#" * width)
    n += 1

#Review
#TODO
My solution results in the same output, but the suggested one uses a loop variable
which is better as we might want to keep the height variable intact for later use 
(e.g. printing out the original height that they did input)
""" 