"""
Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. 
The program should then print out the number of times the user tried different codes.

Sample output
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts

If the user gets it right on the first try, the program should print out something a bit different:

Sample output
PIN: 4321
Correct! It only took you one single attempt!

"""
# Write your solution here
attempts = 0
correct_pin = 4321 #Making a separate variable to make it cleaner to set new pin later on

while True:
    pin = int(input("PIN: "))

    attempts += 1 #As soon as a PIN is entered an attempt has been made, if we put it after conditional statement we miss out on the right attempt

    if pin == correct_pin:
        break

    print("Wrong") #I learned from prev exercises that else statement isn't necessary here

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")

"""
# Suggested solution

attempts = 1
while True:
    pin = input("PIN: ")
    if pin == "4321":
        break
    print("Wrong")
    attempts += 1
 
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
 

#Review
My solution results in the same output, but the suggested one asks for the pin variable in string type,
not sure how this could be beneficial if we work with numeric pins here. Could be necessary if we'd allow non-numeric codes.
It also doesn't use the correct pin in a separate variable like I did,
which makes my code more future proof I think. The suggested solution also assumes a first attempt will be made
which is fine but maybe a bit implicit. 
"""