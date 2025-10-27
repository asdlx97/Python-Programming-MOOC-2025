"""
Please write a program which asks the user for a string 
and then prints it out so that exactly 20 characters are displayed. 

If the input is shorter than 20 characters, 
the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Sample output
Please type in a string: python
**************python

Sample output
Please type in a string: alongerstring
*******alongerstring

Sample output
Please type in a string: averyverylongstring
*averyverylongstring
"""
# Write your solution here
input_string = input("Please type in a string: ")
stars_amount = 20 - len(input_string)

print(f"{'*' * stars_amount}{input_string}")

"""
# Suggested solution

word = input("Please type in a string: ")
 
aligned = (20 - len(word)) * "*" + word
 
print(aligned)

#Review
My solution results in the same output, the suggested one just uses an extra 
variable to store the aligned text before printing.

""" 