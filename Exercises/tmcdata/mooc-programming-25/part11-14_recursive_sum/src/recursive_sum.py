# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    # if the number is 1, there is nothing else to add
    if number <= 1:
        return number

    # fill in the rest of the function
    return number + recursive_sum(number-1)

if __name__ == "__main__":
    result = recursive_sum(3)
    print(result)

    print(recursive_sum(5))
    print(recursive_sum(10))

"""
#Suggested solution

def recursive_sum(number: int):
    # when the number is 1, there are no other summable...
    if number <= 1:
        return number
 
    return number + recursive_sum(number - 1)
    
# WRITE YOUR SOLUTION HERE:
 
#Review
My solution results in the same output, the suggested one is exactly the same.
"""