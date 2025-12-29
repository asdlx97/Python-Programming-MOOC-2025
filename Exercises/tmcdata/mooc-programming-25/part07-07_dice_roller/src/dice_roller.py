"""
In this exercise you will write some functions which can be used in games that involve dice.

Instead of normal dice this exercise specifies non-transitive dice.
You can read up on these here or watch this video.

You will use three dice:

Die A has the sides 3, 3, 3, 3, 3, 6
Die B has the sides 2, 2, 2, 5, 5, 5
Die C has the sides 1, 4, 4, 4, 4, 4
Please write a function named roll(die: str), which rolls the die
specified by the argument. An example of how this should work:

for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")
Sample output
3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  6  3  6  3
2  2  5  2  2  5  5  2  2  5  2  5  5  5  2  5  2  2  2  2
4  4  4  4  4  1  1  4  4  4  1  4  4  4  4  4  4  4  4  4

Also write a function named  play(die1: str, die2: str, times: int),
which throws both dice as many times as specified by the third argument.
The function should return a tuple. The first item should be the number
of times die 1 won, the second the number of times die 2 won, and the
third item should be the number of ties.

result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)
Sample output
(292, 708, 0)
(249, 273, 478)
"""

# Write your solution here
from random import choice


def roll(die: str):
    dies = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}
    return choice(dies[die])


def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for i in range(times):
        die1_result = roll(die1)
        die2_result = roll(die2)

        if die1_result > die2_result:
            die1_wins += 1
        elif die1_result < die2_result:
            die2_wins += 1
        else:
            ties += 1

    return (die1_wins, die2_wins, ties)


if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)

"""
# Suggested solution

from random import sample
def roll(die: str):
    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
 
    return sample(dices[die], 1)[0]
 
def play(die1: str, die2: str, times: int):
    v1 = 0
    v2 = 0
    t = 0
    for i in range(times):
        n1 = roll(die1)
        n2 = roll(die2)
        if n1>n2:
            v1 += 1
        elif n1<n2:
            v2 += 1
        else:
            t += 1
    return v1, v2, t

#Review
My solution results in the same output, the suggested one just uses the 
choice() function from the random module instead of the choice() function like I did.
"""
