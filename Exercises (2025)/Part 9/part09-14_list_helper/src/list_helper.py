"""
Please create a class named ListHelper which contains the following two class methods.

greatest_frequency(my_list: list) returns the most common item on the list
doubles(my_list: list) returns the number of unique items which appear at least twice on the list
It should be possible to use these methods without creating an instance of the class. An example of how the methods could be used:

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
Sample output
5
3
"""


# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        most_common = my_list[0]
        most_amount = 0

        for i in my_list:
            current = i
            amount = 0
            for j in my_list:
                if j == i:
                    amount += 1
            if amount >= most_amount:
                most_amount = amount
                most_common = current

        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        twice = []

        for i in my_list:
            current = i
            amount = 0
            if i not in twice:
                for j in my_list:
                    if j == i:
                        amount += 1
                if amount >= 2:
                    twice.append(i)

        return len(twice)


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

"""
# Suggested solution

class ListHelper:
 
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None
 
        max_frequency = 0
        max_item = None
        for item in my_list:
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency:
                max_frequency = frequency
                max_item = item
 
        return max_item
 
    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)
 
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
 
        return doubles

#Review
My solution results in the same output, suggested uses the .count method
instead of combining two for loops to count the highest frequency and doubles.
I knew there should be a list method that I've forgotten but was on the train so couldn't check the docs.
Also uses the None value as the default highest freq item.
"""
