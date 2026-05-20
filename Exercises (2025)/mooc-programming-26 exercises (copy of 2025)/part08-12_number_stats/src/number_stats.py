# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        else:
            return sum(self.numbers) / len(self.numbers)


stats = NumberStats()
even = NumberStats()
odd = NumberStats()

while True:
    no_input = int(input("Please type in integer numbers:"))

    if no_input == -1:
        break

    stats.numbers.append(no_input)

    if no_input % 2 == 0:
        even.numbers.append(no_input)
    else:
        odd.numbers.append(no_input)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")
