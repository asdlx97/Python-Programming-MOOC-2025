# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, round: int):
        super().__init__(round)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2


class MostVowels(WordGame):
    def __init__(self, round: int):
        super().__init__(round)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouAEIOU"
        words = [
            {"player": "1", "wording": player1_word, "vowels": 0},
            {"player": "2", "wording": player2_word, "vowels": 0},
        ]

        for word in words:
            for char in word["wording"]:
                if char in vowels:
                    word["vowels"] += 1

        if words[0]["vowels"] > words[1]["vowels"]:
            return 1
        elif words[0]["vowels"] < words[1]["vowels"]:
            return 2


class RockPaperScissors(WordGame):
    def __init__(self, round: int):
        super().__init__(round)

    def round_winner(self, p1w: str, p2w: str):
        options = ["rock", "paper", "scissors"]
        if p1w not in options and p2w not in options:
            return None
        elif p1w == p2w:
            return None
        elif p1w in options and p2w not in options:
            return 1
        elif p1w not in options and p2w in options:
            return 2

        if p1w == options[0]:
            if p2w == options[2]:
                return 1
            else:
                return 2

        if p1w == options[1]:
            if p2w == options[0]:
                return 1
            else:
                return 2

        if p1w == options[2]:
            if p2w == options[1]:
                return 1
            else:
                return 2


if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()
