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
