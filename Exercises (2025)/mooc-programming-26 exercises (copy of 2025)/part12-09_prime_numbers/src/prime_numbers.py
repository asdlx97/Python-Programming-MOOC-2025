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
