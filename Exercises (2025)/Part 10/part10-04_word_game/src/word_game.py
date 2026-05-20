"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

The exercise template contains the class definition for a WordGame. It provides some basic functionality for playing different word-based games:

import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
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
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")
The game is played as follows:

p = WordGame(3)
p.play()
Sample output
Word game:
round 1
player1: longword
player2: ??
player 2 won
round 2
player1: i'm the best
player2: wut?
player 1 won
round 3
player1: who's gonna win
player2: me
player 1 won
game over, wins:
player 1: 2
player 2: 1
In this "basic" version of the game the winner is determined randomly. The input from the players has no effect on the result.

Longest word wins

Please define a class named LongestWord. It is a version of the game where whoever types in the longest word on each round wins.

The new version of the game is implemented by inheriting the WordGame class. The round_winner method should also be suitably overridden. The outline of the new class is as follows:

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
An example of how the new game is played:

p = LongestWord(3)
p.play()
Sample output
Word game:
round 1
player1: short
player2: longword
player 2 won
round 2
player1: word
player2: wut?
round 3
player1: i'm the best
player2: no, me
player 1 won
game over, wins:
player 1: 1
player 2: 1
Most vowels wins

Please define another WordGame class named MostVowels. In this version of the game whoever has squeezed more vowels into their word wins the round.

Rock paper scissors

Finally, please define a class named RockPaperScissors which allows you to play a game of rock paper scissors.

The rules of the game are as follows:

rock beats scissors (the rock can break the scissors but the scissors can't cut the rock)
paper beats rock (the paper can cover the rock)
scissors beats paper (the scissors can cut the paper)
If the input from either player is invalid, they lose the round. If both players type in something else than rock, paper or scissors, the result is a tie.

An example of how the game is played:

p = RockPaperScissors(4)
p.play()
Sample output
Word game:
round 1
player1: rock
player2: rock
round 2
player1: rock
player2: paper
player 2 won
round 3
player1: scissors
player2: paper
player 1 won
round 4
player1: paper
player2: dynamite
player 1 won
game over, wins:
player 1: 2
player 2: 1
"""

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


"""
# Suggested solution

import random
 
class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds
 
    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)
 
    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
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
                pass # it's a tie
 
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")
 
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            # Any number can be returned for tie according to
            # definition
            return 0
 
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    #  Help method for calculating the vowels
    def count_vowels(self, word: str):
        vok = "aeiouyåöäö"
        vowels = 0
        for character in word:
            if character in vok:
                vowels += 1
        return vowels
 
 
    def round_winner(self, player1_word: str, player2_word: str):
        if self.count_vowels(player1_word) > self.count_vowels(player2_word):
            return 1
        elif self.count_vowels(player2_word) > self.count_vowels(player1_word):
            return 2
        else:
            return 0
 
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    def round_winner(self, player1_word: str, player2_word: str):
        choices = {"rock" : 0, "paper": 1, "scissors": 2}
        # Not good first
        if player1_word not in choices.keys() and player2_word not in choices.keys():
            return 0
 
        if player1_word not in choices.keys():
            return 2
 
        if player2_word not in choices.keys():
            return 1
 
        # Use dictionary to calculate the difference between
        # choices. For example: player 1 selects paper, value is 1
        # player2 selects rock, value is 0
        # player 1 wins when the difference is 1 or -2
        # player 2 wins when the difference is -1 ot 2
        # 0 means that both selected the same choice
        difference = choices[player1_word] - choices[player2_word]
        
        if difference == 0:
            return 0
 
        if difference == 1 or difference == -2:
            return 1
 
        return 2

#Review
My solution results in the same output, the suggested one creates and
uses a helper method for the MostVowels wordgame. It also uses a much 
more efficiënt way to classify the results of the RockPaperScissor game
by using mathematics besides logic, which is much shorter. 
"""
