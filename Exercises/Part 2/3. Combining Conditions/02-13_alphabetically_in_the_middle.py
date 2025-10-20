"""
Please write a program which asks the user for three letters. 
The program should then print out whichever of the three letters 
would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output
1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output
1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B

"""
#·Write·your·solution·here
letter_1 = input("1st letter: ")
letter_2 = input("2nd letter: ")
letter_3 = input("3rd letter: ")

if (letter_1 > letter_2 and letter_2 > letter_3) or (letter_3 > letter_2 and letter_2 > letter_1):
    print(f"The letter in the middle is {letter_2}")
elif (letter_2 > letter_1 and letter_1 > letter_3) or (letter_3 > letter_1 and letter_1 > letter_2):
    print(f"The letter in the middle is {letter_1}")
else:
    print(f"The letter in the middle is {letter_3}")

"""
# Suggested solution
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
 
if letter1 > letter2 and letter1 > letter3:
    if letter2 > letter3:
        middle = letter2
    else:
        middle = letter3
elif letter2 > letter3:
    if letter3 > letter1:
        middle = letter3
    else:
        middle = letter1
else:
    if letter2 > letter1:
        middle = letter2
    else:
        middle = letter1
 
print("The letter in the middle is " + middle)
 

#Review
My solution results in same output, but the suggested one is using many more nested
conditional statements, which to me seems a bit harder to read and reason about than necessary.

I feel like later on we'll learn about a function that must be able to do this in one line or so, using sorting. 
"""