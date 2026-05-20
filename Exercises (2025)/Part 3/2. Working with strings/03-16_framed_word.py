"""
Please write a program which asks the user for a string and then prints out a frame 
of * characters with the word in the centre. The width of the frame should be 30 characters. 

You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, 
you may print out the word in either of the two possible centre locations.

Sample output
Word: testing
******************************
*          testing           *
******************************

Sample output
Word: python
******************************
*           python           *
******************************

"""
# Write your solution here
input_string = input("Word: ")
left_side_length = (28 - len(input_string))/2
right_side_length = left_side_length

if len(input_string) % 2 != 0:
    right_side_length += 1

print(f"{'*' * 30}")
print(f"*{' ' * int(left_side_length)}{input_string}{' ' * int(right_side_length)}*")
print(f"{'*' * 30}")

"""
# Suggested solution

word = input("Word: ")
 
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
# If the word length is odd, one is added to the spaces at the end of the word
# to get all 30 characters filled
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)

#Review
This exercise is the first one where I had to remediate and tweak more than 5 times!
It's getting challenging finally, but satisfying as my solution results in the same output.

I didn't expect to have generally the same script. I just used / instead of // but my int() conversion did the trick.
Also did I use f-strings in my version.

""" 