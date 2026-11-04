from validations_module import *




def add_team():
    name = get_name()
    id_num = get_id()
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
    return team

def show_all_teams(teams):
    if not teams:
        print("There's no teams available")
        return
    for team in teams:
         print(team["id"], team["name"], team["played"], team["points"])



#checking if "show_all_teams" works
#
# teamssss =[ {
#     "id": 1,
#     "name": "Beit",
#     "played": 3,
#     "wins": 1,
#     "draws": 0,
#     "losses": 0,
#     "goals_for": 0,
#     "goals_against": 0,
#     "points": 20
# },
#  {
#      "id": 2,
#      "name": "TLV",
#      "played": 5,
#      "wins": 1,
#      "draws": 0,
#      "losses": 0,
#      "goals_for": 0,
#      "goals_against": 0,
#      "points": 30
#  }
#  ]
#
# show_all_teams(teamssss)