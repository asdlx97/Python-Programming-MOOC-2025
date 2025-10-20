"""
Please write a program which asks the user for a password. 
The program should then ask the user to type in the password again. 

If the user types in something else than the first password, 
the program should keep on asking until the user types the first password again correctly.

Have a look at the expected behaviour below:

Sample output
Password: sekred
Repeat password: secret
They do not match!
Repeat password: cantremember
They do not match!
Repeat password: sekred
User account created!

"""
# Write your solution here
pwd = input("Password: ")

while True:
    pwdcheck = input("Repeat password: ")
    if pwd == pwdcheck:
        break
    else: #Should I make this a separate if condition?
        print("They do not match!")

print("User account created!")

"""
# Suggested solution

password = input("Password: ")
while True:
    password_again = input("Repeat password: ")
    if password == password_again:
        break
    print("They do not match!")
 
print("User account created!")
 

#Review
My solution results in the same output, but the suggested one doesn't use the else statement 
as it isn't necessary when the if statement ends with a break (or another flow control I guess?).
I think it would only be necessary if there would be one more condition or different print needed.
"""
