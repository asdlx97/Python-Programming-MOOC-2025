# Write your solution to exercise 3 here
def read_points():
    results_per_team = []  # Again I first initialize what I return
    with open("statistics.txt") as new_file:
        line_no = 1
        for line in new_file:
            # First split is for the team and its results
            team_name_and_results_list = line.strip().split(":")
            team_name = team_name_and_results_list[0]
            # Second split is to split types of results

            team_results_list = team_name_and_results_list[1].split("-")
            team_results_list_int = []
            for result in team_results_list:
                try:
                    team_results_list_int.append(int(result))
                except ValueError:
                    return print(f"Invalid format in the file: {line}")

            team_points = (
                (team_results_list_int[0] * 3)
                + (team_results_list_int[1] * 0)
                + (team_results_list_int[2] * 1)
            )  # I did multiply tie by one just for clarity
            # Putting "three points for a win, one point for a tie, and no points for a loss" in the exercise was a bit misleading if given list contains the following order [wins, losses, ties]

            results_per_team.append((team_name, team_points))

            line_no += 1
    return results_per_team


if __name__ == "__main__":
    print(read_points())
