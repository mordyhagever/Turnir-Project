from validations_module import *
from data_base import *
from tables_manager import calc_points, goals_updator

def get_groups_id():
    print("Enter first group details")
    home_group_id = get_id()
    while is_id_available(home_group_id):
        print("i'd doesn't exist") #the id doesn't exist in the list
        home_group_id = get_id()
    print("Enter second group details")
    outsider_group_id = get_id()
    while is_id_available(outsider_group_id) or not is_different_team(home_group_id, outsider_group_id):
        print("id doesn't exist, or second group has the same id:\n")
        outsider_group_id = get_id()
    return home_group_id, outsider_group_id


def groups_goals():
    team1_goals = input("Enter amount of goals for first team")
    team1_goals = string_to_int(team1_goals)
    while not is_goals_legal(team1_goals):
        team1_goals = input("Enter non negative goals:\n")
        if is_goals_legal(team1_goals):
            team1_goals = string_to_int(team1_goals)
    team2_goals = input("Enter amount of goals for second team:\n")
    team2_goals = string_to_int(team2_goals)
    while not is_goals_legal(team2_goals):
        team2_goals = input("Enter non negative goals:\n")
        if is_goals_legal(team1_goals):
            team2_goals = string_to_int(team2_goals)
    return team1_goals, team2_goals

def is_allowed_to_play(group1, group2):
    for matches in all_games:
        if matches["home_group"] == group1 and matches["outsider_group"] == group2 or matches["home_group"] == group2 and matches["outsider_group"] == group1:
            return False
    return True


def add_game_main():
    teams = get_groups_id()
    while not is_allowed_to_play(teams[0], teams[1]):
        print("teams already played together!")
        teams = get_groups_id()
    goals = groups_goals()
    if goals[0] > goals[1]:
        winning_team = teams[0]
        losing_team = teams[1]
    elif goals[1] > goals[0]:
        winning_team = teams[1]
        losing_team = teams[0]
    else:
        winning_team = (teams[0], teams[1])
        losing_team = None
    calc_points(winning_team, losing_team)
    goals_updator(teams[0], goals[0], teams[1], goals[1])

    all_games.append({"home_group": teams[0], "outsider_group": teams[1], "home_goals": goals[0], "outsider_goals": goals[1]})
    return "Match has been updated"

# print(add_game_main())


