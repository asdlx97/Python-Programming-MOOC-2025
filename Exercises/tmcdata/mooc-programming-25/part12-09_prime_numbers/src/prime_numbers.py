"""
A prime number is a number which is divisible only by itself and the number 1. By convention prime numbers are defined as positive integers from the number 2 upwards. The first six prime numbers are 2, 3, 5, 7, 11 and 13.

Please write a generator function prime_numbers() which creates a new generator. The generator should return new prime numbers, one by one in sequence, from 2 onwards. NB: this generator never terminates. It will generate numbers for as long as they are needed.

For example:

numbers = prime_numbers()
for i in range(8):
    print(next(numbers))

Sample output
2
3
5
7
11
13
17
19
Hint: you can use a loop to check if a number is a prime number. If we are checking the number x, the loop would go through the numbers 2 to x-1. If x is divisible by any one of these, it is not a prime number.
"""


# Write your solution here
def prime_numbers():
    number = 2
    while True:
        prime = True
        for no in range(2,number):
            if number % no == 0:
                prime = False
        if prime:
            yield number
        number += 1

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))

"""
#Suggested solution

def prime_numbers():
    number = 1
    while True:
        if is_prime(number):
            yield number
        number += 1
 
# Helper method for checking if number is prime
def is_prime(number: int):
    if number < 2:
        return False
    # Possible divisor is between 2 and number-1
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
 

#Review
My solution results in the same output, the suggested one takes a uses
a helper function to check if its a prime number.
"""