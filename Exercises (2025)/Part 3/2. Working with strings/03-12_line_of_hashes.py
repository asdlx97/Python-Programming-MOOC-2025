"""
Please write a program which prints out a line of hash characters, 
the width of which is chosen by the user.

Sample output
Width: 3
###

Sample output
Width: 8
########

"""
# Write your solution here
measure = "#"
width = int(input("Width: "))

print(measure*width)

"""
# Suggested solution

width = int(input("Width: "))
 
print("#"*width)

#Review
My solution results in the same output, the suggested one uses one less variable and
puts the # directly within the print statement. I like it in a separate one as it's
a bit easier to replace if needed. 
""" 