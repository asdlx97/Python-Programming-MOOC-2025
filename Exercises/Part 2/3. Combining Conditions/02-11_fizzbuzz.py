"""
Please write a program which asks the user for an integer number. 
If the number is divisible by three, the program should print out Fizz. 
If the number is divisible by five, the program should print out Buzz. 
If the number is divisible by both three and five, the program should print out FizzBuzz.

Some examples of expected behaviour:

Sample output
Number: 9
Fizz

Sample output
Number: 7

Sample output
Number: 20
Buzz

Sample output
Number: 45
FizzBuzz

"""
# Write your solution here
integer = int(input("Number: "))

if (integer / 3) == (integer // 3) and (integer / 5) == (integer // 5): #Using division with integer result to compare to division with float result
    print("FizzBuzz")
elif float(integer / 5) == int(integer / 5): #Using another way to compare by converting to integer
    print("Buzz")
elif integer % 3 == 0: #Using modulo as in suggested solution, which is the cleanest way 
    print("Fizz")

"""
# Suggested solution
number = int(input("Number: "))
 
if number % 3 == 0 and number % 5 == 0:
    # This condition must be evaluated first, because if this is true,
    # also both of the following conditions are true
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
 


#Review
My solution results in same output, but the suggested one uses modulo for comparision,
which makes more sense but I forgot about its existance. I adjusted the last statement to use modulo.
"""
