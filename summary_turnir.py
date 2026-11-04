from data_base import *
from tables_manager import leading_team

def summary():
    sum_all = {}
    num_of_teams = len(all_teams)
    num_of_games = len(all_games)
    num_of_goals = 0
    average_goals = 0
    tie_games = 0
    leading = leading_team()
    for team in all_teams:
        if team["goals_for"] > 0:
            num_of_goals += team["goals_for"]
    for game in all_games:
        if game["home_goals"] == game["outsider_goals"]:
            tie_games += 1
    average_goals = num_of_goals / num_of_games
    sum_all["num_of_teams"] = num_of_teams
    sum_all["num_of_games"] = num_of_games
    sum_all["num_of_goals"] = num_of_goals
    sum_all["average_goals"] = average_goals
    sum_all["tie games"] = tie_games
    sum_all["leading_team"] = leading
    return sum_all


