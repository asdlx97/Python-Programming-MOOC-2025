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
