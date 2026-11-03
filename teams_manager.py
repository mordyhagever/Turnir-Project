from validations import *

def add_team():
    name = str(input("Please enter a group team"))
    while not check_name(name):
        name = str(input("Please enter a group team"))
    id_num = input("please enter a positive id")
    while not check_id(id_num):
        id_num = input("please enter a positive and full number")
    team = {
        "id": id_num,
        "name": id_num,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }



