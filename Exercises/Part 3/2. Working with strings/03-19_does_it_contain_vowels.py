"""
Please write a program which asks the user to input a string. 
The program then prints out different messages if the string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

Sample output
Please type in a string: hello there
a not found
e found
o found

Sample output
Please type in a string: hiya
a found
e not found
o not found

"""
# Write your solution here
input_string = input("Please type in a string: ")
check = "aeo"
loop_variable = 0

while loop_variable < len(check):
    substring = check[loop_variable]
    if substring in input_string:
        print(f"{substring} found")
    else:
        print(f"{substring} not found")
    
    loop_variable += 1

"""
# Suggested solution

string = input("Please type in a string: ")
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1

#Review
Same script, same output!!! I wouldv'e never thought that as I see other ways this could be
done but I found mine to be the most elegant. And this happens to be the suggested solutin as well, hyped!

#TODO Rewrite this print statement with the shorter if else one line syntax later
""" 