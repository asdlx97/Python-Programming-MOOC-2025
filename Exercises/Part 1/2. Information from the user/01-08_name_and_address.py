# # More than one input with several variables
# name = input("What is your name? ")
# email = input("What is your email address? ")
# nickname = input("What is your nickname? ")

# print("Let's make sure we got this right")
# print("Your name: " + name)
# print("Your email address: " + email)
# print("Your nickname: " + nickname)

# # Same variable's value will be replaced when assigned new value
# address = input("What is your address? ")
# print("So you live at address " + address)

# address = input("Please type in a new address: ")
# print("Your address is now " + address)

# Exercise
# Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:

# Sample output
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

givenName = input("What's your given name?")
familyName = input("What's your family name?")
streetAddress = input("What's your street address?")
cityPostalCodeAddress = input("What's your city and postal code?")

print(givenName + " " + familyName)
print(streetAddress)
print(cityPostalCodeAddress)