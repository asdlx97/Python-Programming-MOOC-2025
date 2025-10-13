"""
Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. 
If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

Two examples of expected behaviour:

Sample output
Please type in a temperature (F): 101
101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

Please type in a temperature (F): 21
21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
Brr! It's cold in here!

"""
# Write your solution here
degreesFeirenheit = int(input("Please type in a temperature (F): "))

degreesCelcius = (degreesFeirenheit - 32) * (5 / 9)

print(f"{degreesFeirenheit} degrees Fahrenheit equals {degreesCelcius} degrees Celsius")

if degreesCelcius < 0:
    print("Brr! It's cold in here!")

"""
#Suggested Solution

temperature_f = int(input("Please type in a temperature (F): "))
 
temperature_c = (temperature_f - 32) * 5/9
 
print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
 
if temperature_c < 0:
    print("Brr! It's cold in here!")

#Review
Same result, same script.
"""