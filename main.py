from teams_manager import *
from validations_module import *
from games_manager import *
from tables_manager import *
from summary_turnir import *

def active1():
    add_team()
def active2():
    show_all_teams()
def active3():
    return add_game_main()
def active4():
    return create_table(print_tables_menu())
def active5():
    return leading_team()
def active6():
    return best_attacking_team()
def active7():
    return best_success_rate()
def active8():
    return teams_without_wins()
def active9():
    return summary()
def active10():
    pass


def print_menu():
    print("""========== Tournament Manager ==========")
    1. Add team
    2. Show all teams
    3. Add match result
    4. Show standing
    5. Show leading team
    6. Show best attacking team
    7. Show team success rate
    8. Show teams without wins
    9. Show tournament summary
    10. check championship potential
    0. exit
""")
    choose = input()
    while not check_menu(choose):
        choose = input("only number between 0 and 10")
    choose = string_to_int(choose)
    return choose

def active_system():
    while True:
        choose = print_menu()
        if choose == 1:
            active1()
        elif choose == 2:
            active2()
        elif choose == 3:
            print(active3())
        elif choose == 4:
            print(active4())
        elif choose == 5:
            print(active5())
        elif choose == 6:
            print(active6())
        elif choose == 7:
            print(active7())
        elif choose == 8:
            print(active8())
        elif choose == 9:
            print(active9())
        elif choose == 10:
            active10()
        elif choose == 0:
            break
    return "Finished progress"

print(active_system())



# print_menu()