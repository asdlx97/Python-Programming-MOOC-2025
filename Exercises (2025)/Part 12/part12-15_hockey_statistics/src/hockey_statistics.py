"""
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

In this exercise you will build an application for examining hockey league statistics from the NHL in a couple of different ways.

The exercise template contains two JSON files: partial.json and all.json. The first of these is mostly meant for testing. The latter contains a lot of data, as all the NHL player stats for the 2019-20 season are included in the file.

The entry for a single player is in the following format:

{
    "name": "Patrik Laine",
    "nationality": "FIN",
    "assists": 35,
    "goals": 28,
    "penalties": 22,
    "team": "WPG",
    "games": 68
}
Both files contain a list of entries in the above format.

If you need a refresher on handling JSON files, please take a look at part 7 of this course material.

Search and list

Please write an interactive application which first asks for the name of the file, and then offers the following functions:

search by name for a single player's stats
list all the abbreviations for team names in alphabetical order
list all the abbreviations for countries in alphabetical order
These functionalities grant you one exercise point. Your application should now work as follows:

Sample output
file name: partial.json
read the data of 14 players

commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

command: 1
name: Travis Zajac

Travis Zajac         NJD   9 + 16 =  25
command: 2
BUF
CGY
DAL
NJD
NYI
OTT
PIT
WPG
WSH

command: 3
CAN
CHE
CZE
SWE
USA

command: 0
NB: the printout format for a player must be exactly as follows:

Sample output
Leon Draisaitl       EDM  43 + 67 = 110
Connor McDavid       EDM  34 + 63 =  97
Travis Zajac         NJD   9 + 16 =  25
Mike Green           EDM   3 +  8 =  11
Markus Granlund      EDM   3 +  1 =   4
123456789012345678901234567890123456789
The last line in the sample above is there to help you calculate the widths of the different fields in the output; you should not print the numbers line yourself in your final submission.

The abbreviation for the team is printed from the 22nd character onwards. The + sign is the 30th character and the = sign is the 35th character. All the fields should be justified to the right edge. All whitespace is space characters.

F-strings are probably the easiest way to achieve the required printout. The process is similar to this exercise from part 6.

List players by points

These two functionalities will grant you a second exercise point:

list players in a specific team in the order of points scored, from highest to lowest. Points equals goals + assists
list players from a specific country in the order of points scored, from highest to lowest
Your application should now work as follows:

Sample output
file name: partial.json
read the data of 14 players

commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

command: 4
team: OTT

Drake Batherson      OTT   3 +  7 =  10
Jonathan Davidsson   OTT   0 +  1 =   1
command: 5
country: CAN

Jared McCann         PIT  14 + 21 =  35
Travis Zajac         NJD   9 + 16 =  25
Taylor Fedun         DAL   2 +  7 =   9
Mark Jankowski       CGY   5 +  2 =   7
Logan Shaw           WPG   3 +  2 =   5
command: 0
Most successful players

These two functionalities will grant you a third exercise point:

list of n players who've scored the most points
if two players have the same score, whoever has scored the higher number of goals comes first
list of n players who've scored the most goals
if two players have the same number of goals, whoever has played the lower number of games comes first
Your application should now work as follows:

Sample output
file name: partial.json
read the data of 14 players

commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals

command: 6
how many: 2

Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
command: 6
how many: 5

Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
John Klingberg       DAL   6 + 26 =  32
Travis Zajac         NJD   9 + 16 =  25
Conor Sheary         BUF  10 + 13 =  23
command: 7
how many: 6

Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
Conor Sheary         BUF  10 + 13 =  23
Travis Zajac         NJD   9 + 16 =  25
John Klingberg       DAL   6 + 26 =  32
Mark Jankowski       CGY   5 +  2 =   7
command: 0
"""

# Write your solution here
import json

def read_file(filename):
    with open(filename) as my_file:
        data = my_file.read()
    return json.loads(data)

def help():
    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")
    print()

def print_player(player: dict):
    print(f"{player['name']:21}{player['team']:5}{player['goals']:>2} + {player['assists']:>2} = {player['goals'] + player['assists']:>3}")

def search_for_player(name: str, players: list):
    return [player for player in players if player["name"] == name]

def all_teams(players: list):
    return sorted(set([player["team"] for player in players]))

def players_from_team(team: str, players: list):
    return [player for player in players if player["team"] == team]

def players_from_nationality(nationality: str, players: list):
    return [player for player in players if player["nationality"] == nationality]

def sort_by_score(players: list):
    return sorted(players, key=lambda p:p["assists"]+p["goals"], reverse=True)

def all_countries(players: list):
    return sorted(set([player["nationality"] for player in players]))

def n_players_most_points(n: int, players: list):
    return sorted(players, key=lambda p:(p["assists"]+p["goals"], p["goals"]), reverse=True)[0:n]

def n_players_most_goals(n: int, players: list):
    return sorted(players, key=lambda p:(p["goals"], -p["games"]), reverse=True)[0:n]

def execute():
    filename = input("file name: ")
    players = read_file(filename)
    print(f"read the data of {len(players)} players\n")
    help()
    while True:
        command = input("command: ")
        if command == "1":
            name = input("name: ")
            for player in search_for_player(name, players):
                print_player(player)
            print()
        if command == "0":
            break
        if command == "2":
            for team in all_teams(players):
                print(team)
            print()
        if command == "3":
            for country in all_countries(players):
                print(country)
            print()
        if command == "4":
            team = input("team: ")
            players = players_from_team(team, players)
            for player in sort_by_score(players):
                print_player(player)
            print()
        if command == "5":
            country = input("country: ")
            players = players_from_nationality(country, players)
            for player in sort_by_score(players):
                print_player(player)
            print()
        if command == "6":
            n = int(input("how many: "))
            for player in n_players_most_points(n, players):
                print_player(player)
            print()
        if command == "7":
            n = int(input("how many: "))
            for player in n_players_most_goals(n, players):
                print_player(player)
            print()

execute()

"""
#Suggested solution

import json
 
class Statistics:
    def __init__(self, players: list):
        self.__players = players
 
    def by_points(self,  p):
        return  p['goals'] + p['assists']
 
    def by_goals(self,  p):
        # if the numbe of goals is equal, less played games is better
        return (p['goals'], -p['games'])
 
    def player_data(self, name: str):
        for player in self.__players:
            if player['name'] == name:
                return player
 
        return None
 
    def countries(self):
        return sorted(list(set(p['nationality'] for p in self.__players )))
 
    def teams(self):
        return sorted(list(set(p['team'] for p in self.__players )))
 
    def players_in_team(self, team: str):
        players = [ p for p in self.__players if p['team'] == team]
        return sorted(players, key=self.by_points, reverse=True)
 
    def players_from_country(self, country: str):
        players = [ p for p in self.__players if p['nationality'] == country]
        return sorted(players, key=self.by_points, reverse=True)
 
    def most_points(self, countryra):
        players = sorted(self.__players, key=self.by_points, reverse=True)
        return players[0: countryra]
 
    def most_goals(self, countryra):
        players = sorted(self.__players, key=self.by_goals, reverse=True)
        return players[0: countryra]
 
class Application:
    def __init__(self):
        self.__statistics = None
 
    def instructions(self):
        instructions = 
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals
        print(instructions)
 
    def f(self, p: dict):
        """
            helper method, which creates a string out of players formatted for output
        """
        points = p['goals'] + p['assists']
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
 
    def read_file(self):
        file_name = input("file: ")
        with open(file_name) as file:
            data = file.read()
 
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.__statistics = Statistics(players)
 
    def get_playes(self):
        name = input("name: ")
        player = self.__statistics.player_data(name)
        if player:
            print(self.f(player))
 
    def get_teams(self):
        for team in self.__statistics.teams():
            print(team)
 
    def get_countries(self):
        for country in self.__statistics.countries():
            print(country)
 
    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(self.f(player)) 
 
    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(self.f(player)) 
 
    def most_points(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_points(number):
            print(self.f(player)) 
 
    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_goals(number):
            print(self.f(player)) 
 
    def execute(self):
        self.read_file()
        self.instructions()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.get_playes()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
 
Application().execute()


 
#Review
My solution results in the same output, the suggested one uses
an object-oriënted approach, while I mainly kept it at just functions
but I could easily convert this.
"""

