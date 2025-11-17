"""
Please write a function named factorials(n: int),
which returns the factorials of the numbers 1 to n in a dictionary.
The number is the key, and the factorial of that number is the value mapped to it.

A reminder: the factorial of the number n is written n! and is calculated by
multiplying the number by each integer smaller than itself. For example,
the factorial of 4 is 4 * 3 * 2 * 1 = 24.

An example of the function in action:

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])

Sample output
1
6
120
"""


# Write your solution here
def factorials(n: int):
    factorials = {}

    for i in range(1, n + 1):
        factorial = 1
        for j in range(i):
            factorial += factorial * j
        factorials[i] = factorial

    return factorials


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])


"""
# Suggested Solution

def factorials(n: int):
    result = {}
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i-1] * i
    return result

#Review
My solution produces the correct output, but it’s more computationally heavy 
and less precise in logic I'd say. The suggested version is structurally smarter as 
it uses the previously computed factorial (result[i-1]) to calculate the next one, 
avoiding an unnecessary inner loop. This makes it both more efficient and more readable.
"""
