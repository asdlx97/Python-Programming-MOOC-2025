"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

The exercise template contains the definition for a class named BallPlayer. It has the following public attributes:

name
shirt number number
scored goals goals
assists completed assists
minutes played minutes
Please implement the following functions. NB: each function has a different type of return value.

Most goals

Please write a function named most_goals which takes a list of ball players as its argument.

The function should return the name of the player who scored the most goals, in string format.

Most points

Please write a function named most_points, which takes a list of ball players as its argument.

The function should return a tuple containing the name and shirt number of the player who has scored the most points. The total number of points is the number of goals and the number of assists combined.

Least minutes

Please write a function named least_minutes, which takes a list of ball players as its argument.

The function should return the BallPlayer object which has the smallest value of minutes played.

You can test your functions with the following program:

if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))
This should print out:

Sample output
Archie Bonkers
('Cruella De Hill', 9)
BallPlayer(name=Donald Quack, number=4, goals=3, passes=9, minutes=12)
"""


class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(players: list):
    return sorted(players, key=lambda player: player.goals, reverse=True)[0].name

def most_points(players: list):
    player = sorted(players, key=lambda player: player.goals + player.passes, reverse=True)[0]
    return (player.name, player.number) 

def least_minutes(players: list):
    return sorted(players, key=lambda player: player.minutes, reverse=False)[0]
    

if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))

"""
#Suggested solution

class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes
 
    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')
 
 
def most_goals(ballplayers: list):
    return max(ballplayers, key=lambda p: p.goals).name
 
def most_points(ballplayers: list):
    best = max(ballplayers, key=lambda p: p.goals + p.passes)
    return (best.name, best.number)
 
def least_minutes(ballplayers: list):
    return min(ballplayers, key=lambda p: p.minutes)
 

#Review
My solution results in the same output, the suggested one is a bit 
more pythonic in the sense that it uses the built in max() and min()
functions instad of sorted() with reverse True/False argument.
"""