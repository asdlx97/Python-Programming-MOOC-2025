"""
The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

2
45
108
3
-10
1100
...etc...

Please write a function named largest, which reads the file and returns the largest
number in the file.

Notice that the function does not take any arguments. The file you are working with
is always named numbers.txt.

NB: If Visual Studio Code can't find the file and you have checked that there are
no spelling errors, take a look at the instructions following this exercise.
"""


# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = 0

        for number in new_file:
            number = int(number)
            if number > largest:
                largest = number

    return largest


if __name__ == "__main__":
    largest()

"""
# Suggested solution

def largest():
    with open("numbers.txt") as file:
        start = True
        biggest = 0
        for number in file:
            if start or int(number) > biggest:
                biggest = int(number)
                start = False
        return biggest
    
#Review
My solution gives the correct result, but it makes an assumption that all 
numbers in the file are non-negative by initializing largest = 0. 
The suggested solution avoids this limitation by using a start flag to 
ensure the first number in the file always sets the initial value which 
is making it more robust for files that might contain only negative numbers.
 """
