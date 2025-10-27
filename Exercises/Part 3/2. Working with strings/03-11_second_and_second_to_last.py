"""
Please write a program which asks the user for a string. 
The program then prints out a message based on whether 
the second character and the second to last character are the same or not. 

See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a

"""
# Write your solution here
input_string = input("Please type in a string: ")
result = ""

if input_string[1] == input_string[-2]:
    result = f"{input_string[1]}"
else:
    result = "different"

print(f"The second and the second to last characters are {result}")

"""
# Suggested solution

word = input("Please type in a string: ")
 
# Check also that the word is at least two characters long,
# so that the second and second to last characters exist
if len(word) > 1 and word[1] == word[-2]:
    print("The second and the second to last characters are " + word[1])
else:
    print("The second and the second to last characters are different")

#Review
My solution results in the same output, the suggested one makes an additional check
to make sure there is no index out of range error.
""" 