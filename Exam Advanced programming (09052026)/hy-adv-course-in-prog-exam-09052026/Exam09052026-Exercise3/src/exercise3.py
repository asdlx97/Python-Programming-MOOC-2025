# Write your solution to exercise 3 here
from random import randint


class Dice:
    def __init__(self, sides: int = 6):
        self._sides = sides

    def roll_dice(self, times: int):
        return [
            randint(1, self._sides) for i in range(times)
        ]  # Using list comprehension but mayeb could be simplified? I don't know what the i is for, doesn't get used but necessary for syntax?

    def __str__(self):
        return f"{self._sides}-sided dice"


class DiceGame:
    def __init__(self, dice: Dice):
        self.__dice = dice

    def roll_once(self):
        results = []
        for i in range(5):
            results.append(self.__dice.roll_dice(1)[0])
        # result = [self.__dice.roll_dice(1)[0] for i in range(5)]
        if min(results) == max(results):
            print("Yatzy!")
        else:
            print(
                f"Rolled 5 dice and got {', '.join([str(result) for result in results])}."
            )
        return results

    def roll_five_of_a_kind(self):
        rolls = 0
        while True:
            rolls += 1
            results = []
            for i in range(5):
                results.append(self.__dice.roll_dice(1)[0])
            if min(results) == max(results):
                print(f"It took {rolls} rolls to get five of a kind.")
                break

    def __str__(self):
        return f"The goal of the game is to roll the dice and get 5 of the same number. Using {self.__dice}."


if __name__ == "__main__":
    six_sided_dice = Dice()
    game = DiceGame(six_sided_dice)

    print(game)

    game.roll_once()
    game.roll_once()
    game.roll_once()
    game.roll_once()

    game.roll_five_of_a_kind()

    difficult_game = DiceGame(Dice(10))
    difficult_game.roll_five_of_a_kind()

    easy_game = DiceGame(Dice(1))
    easy_game.roll_once()
    easy_game.roll_once()
    easy_game.roll_once()
    easy_game.roll_once()
