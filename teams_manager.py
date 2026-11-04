from validations_module import *
from data_base import all_teams



def add_team():
    id_num = get_id()
    while not is_id_available(id_num):
        print("id is already taken")
        id_num = get_id()
    name = get_name()
    while not is_name_available(name):
        print("name is already taken")
        name = get_name()
    team = {
        "id": id_num,
        "name": name,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }
    all_teams.append(team)
    print("group was successfully added")

def show_all_teams():
    if not all_teams:
        print("There's no teams available")
        return
    for team in all_teams:
         print(f"Team ID: {team["id"]}, Team name: {team["name"]}, Number of games: {team["played"]}, Team score: {team["points"]}")


