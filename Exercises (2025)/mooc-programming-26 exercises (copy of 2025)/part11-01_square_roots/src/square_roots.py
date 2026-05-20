from math import sqrt


# WRITE YOUR SOLUTION HERE:
def square_roots(numbers: list):
    return [sqrt(x) for x in numbers]


if __name__ == "__main__":
    lines = square_roots([1, 2, 3, 4])
    for line in lines:
        print(line)
