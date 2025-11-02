"""
Please write a function named mean, which takes three integer arguments. 
The function should print out the arithmetic mean of the three arguments.

mean(5, 3, 1)
mean(10, 1, 1)

Sample output
3.0
4.0
"""
# Write your code here
def mean (x,y,z):
    print((x+y+z)/3)
# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)

"""
# Suggested solution

def  mean(number1, number2, number3):
    answer = (number1 + number2 + number3) / 3
    print(answer)
 
if __name__ == "__main__":
     mean(1, 2, 3)

#Review
Same script, same output. Suggested one just defines an extra variable inbetween.

""" 