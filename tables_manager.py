from data_base import *
from validations_module import *

def calc_points(winning_team, losing_team):
    if isinstance(winning_team, tuple):
        group1 = winning_team[0]
        group2 = winning_team[1]
        for team in all_teams:
            if team["id"] == group1 or team["id"] == group2:
                team["points"] += 1
                team["draws"] += 1
    else:
        for team in all_teams:
            if team["id"] == winning_team:
                team["points"] += 3
                team["wins"] += 1
            if team["id"] == losing_team:
                team["losses"] += 1

    return "points has been updated"

def goals_updator(group1, goals1, group2, goals2):
    for team in all_teams:
        if team["id"] == group1:
            team["goals_for"] += goals1
            team["goals_against"] += goals2
        if team["id"] == group2:
            team["goals_for"] += goals2
            team["goals_against"] += goals1
    return "goals for and against has been updated"

def print_tables_menu():
    print("""Choose a table:
1. highest points
2. sum of goals (positive minus negative)
3. highest goals_for
4. Alphabet 
    """)
    choose = input()
    while not chack_tables_menu(choose):
        choose = input("choose a valid number:\n")
    choose = string_to_int(choose)
    return choose

def create_table(choose):
    table = None
    if choose == 1:
        table = sorted(all_teams, key=lambda p: p["points"], reverse=True)
    elif choose == 2:
        table = sorted(all_teams, key=lambda p: p["goals_for"] - p["goals_against"], reverse=True)
    elif choose == 3:
        table = sorted(all_teams, key=lambda p: p["goals_for"], reverse=True)
    elif choose == 4:
        table = sorted(all_teams, key=lambda p: p["name"])
    return table

def leading_team():
    lead = create_table(1)
    return lead[0]

def best_attacking_team():
    lead = create_table(3)
    return f"best attacking is: {lead[0]}"

def best_success_rate():
    team = str(input("Enter name"))
    while not check_name(team):
        team = str(input("Enter name:\n"))
    for group in all_teams:
        if group["name"] == team:
            if group["wins"] == 0:
                return "No Games"
            success = 100 * (group["points"] / 3 * group["played"])
            return success
    return "No Games"


def teams_without_wins():
    groups_without_wins = []
    for i in range(len(all_teams)):
        if all_teams[i]["wins"] == 0 and all_teams[i]["played"] > 0:
            groups_without_wins.append(all_teams[i])
    return groups_without_wins



