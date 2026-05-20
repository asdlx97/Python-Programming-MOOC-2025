"""
Please change the program from the previous exercise so that the user gets to input also the base which is multiplied 
(in the previous program the base was always 2).

Sample output
Upper limit: 27
Base: 3
1
3
9
27

Sample output
Upper limit: 1234567
Base: 10
1
10
100
1000
10000
100000
1000000

Please don't use the value True as the condition of your while loop in this exercise!

"""
#·Write·your·solution·here
upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 1

while number <= upper_limit:
    print(number)

    number *= base

"""
# Suggested solution

limit = int(input("Upper limit: "))
multiplier = int(input("Base: "))
number = 1
while number <= limit:
    print(number)
    number *= multiplier
    
#Review
Same output, same script as suggested solution.
"""  