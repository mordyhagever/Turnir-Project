from data_base import all_teams, all_games


def string_to_int(string):
    try:
        string = int(string)
        return string
    except ValueError:
        return "Error, Can't convert to string"

def is_different_team(group1, group2):
    if group1 == group2:
        return False
    return True

def check_id(number) -> bool:
    try:
        number = int(number)
        if number < 1:
            return False
        return True
    except ValueError:
        return False

def check_name(name):
    if len(name) <= 0:
        return False
    return True

def is_id_available(group_id):
    if not all_teams:
        return True
    for group in all_teams:
        if group["id"] == group_id:
            return False
    return True

def is_name_available(group_name):
    if not all_teams:
        return True
    for group in all_teams:
        if group["name"] == group_name:
            return False
    return True



def get_name():
    name = str(input("Please enter a group name: "))
    while not is_name_available(name):
        name = str(input("The name is taken, enter a different name: "))
    while not check_name(name):
        name = str(input("Please enter a valid not empty name: "))
    return name


def get_id():
    id_num = input("please enter a positive id:\n")
    while not check_id(id_num):
        id_num = input("please enter a positive and full number\n")
    id_num = string_to_int(id_num)  #converting to int, after checking it's a number
    return id_num

def is_goals_legal(goals):
    try:
        if int(goals) >= 0:
            return True
    except ValueError:
        return False


def check_menu(num):
    while not check_id(num):
        return False
    num = string_to_int(num)
    if num > 10 or num < 0:
        return False
    return True

def chack_tables_menu(number):
    try:
        number = int(number)
        if number < 1 or number > 5:
            return False
        return True
    except ValueError:
        return False