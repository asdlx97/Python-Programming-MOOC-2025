"""
Please write a function named read_input, which asks the user for input
until the user types in an integer which falls within the bounds given as
arguments to the function. The function should return the final valid integer
value typed in by the user.

An example of the function in action:

number = read_input("Please type in a number: ", 5, 10)
print("You typed in:", number)

Sample output
Please type in a number: seven
You must type in an integer between 5 and 10
Please type in a number: -3
You must type in an integer between 5 and 10
Please type in a number: 8
You typed in: 8
"""


# Write your solution here
def read_input(number: int, min: int, max: int):
    while True:
        try:
            input_str = input("Please type in a number: ")
            number = int(input_str)
            if number >= min and number <= max:
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {min} and {max}")


"""
# Suggested solution

def read_input(prompt: str, lower_limit: int, upper_limit: int):
    while True:
        error = False
        try:
            number = int(input(prompt))
            if number < lower_limit or number > upper_limit:
                error = True
        except:
            error = True
        if error:
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")
        else:
            return number
 
#Review
My solution returns the same output, suggested one structures the error flag a bit
differently.
 """
