# this is a databse 
import os, sys
import sqlite3
from getpass import getpass

import sql_functs

DB_FILE = "val.db"
PROMPT = "->"

# spaces terminal to clear it
def clear_term():
    print(chr(27) + "[2J")

# Function to show and wait for key press 
def waitKey():
    print("Press any key to continue...", end="")
    os.system('pause')
    print()

# main menu u first get
def main_menu():
    clear_term()
    choice = 'TBD'

    options = {
        '1': "Add Game",
        '2': "View/Update Games",
        '3': "Add Player",
        '4': "View/Update Player",
        '5': "Add Team",
        '6': "View/Update Team",
        '7': "View Total Number of Games",
        'q': "",
        'quit': "",
    }

    while(choice != 'q' and choice != 'quit'):
        clear_term()
        print("Please choose from the options below: ")
        for option, desc in options.items():
            if option in ['q', 'quit']:
                continue
            print(option + ". " + desc)
        choice = input(PROMPT)

        if choice not in options.keys():
            print("Invalid choice. Choose from the options below:")
            continue 

        # Add game
        if choice == '1':
            choice = "TBD"
            game = []
            #actually do these
            a = int(input("Please enter animal cage number:\n" + PROMPT))
            b = input("Please enter animal class:\n" + PROMPT)                
            c = input("Please enter animal species:\n" + PROMPT)
            d = input("Please enter animal feed time:\n" + PROMPT)
            e = input("Please enter animal zoo section:\n" + PROMPT)
            f = input("Please enter animal diet:\n" + PROMPT)
            # to here
            game.append([a,b,c,d,e,f])
            sql_functs.add_game(DB_FILE, game)            
            waitKey()
        # View/Update Games
        elif choice == '2':
            choice = "TBD"
            menu_games()
            waitKey()
        # Add player
        elif choice == '3':
            choice = "TBD"

            waitKey()
        # View/Update Player
        elif choice == '4':
            choice = "TBD"
            menu_players()
            waitKey()
        # Add Team
        elif choice == '5':
            choice = "TBD"

            waitKey()
        # View/Update teams
        elif choice == '6':
            choice = "TBD"
            menu_teams()
            waitKey()
        # View num games
        elif choice == '7':
            choice = "TBD"

            waitKey()
    return choice


def menu_games():
    pass
def menu_players():
    pass
def menu_teams():
    pass

    Team_name = input("What is the team name?")
    Winning_team = input("What is the name of the winning team?")
    Map = input("What map did you play?")
    MST_final_score = int(input("what was the MST final score?"))
    Other_team_final_score = int(input("What was the score of the opposing team?"))
    Tournament = input("What tournament was this?")
    #Game_num = int(input("Give me a number that hasn't been given yet")) #might add var to use this
    First = input("What is the manager's first name?")
    Last = input("What is the manager's last name?")
    
    KPR = int(input("What are the KPRs?"))
    Rounds_survived = int(input("How many rounds were survived?"))
    Kills = int(input("How many kills?"))
    Deaths = int(input("How many deaths?"))
    Assists = int(input("How many assists?"))
    Agent = input("What agent?")
    IGN = input("Who is the IGN?")
    Rank = input("What is the rank?")
    IRL_name = input("What is their IRL name?")
    Role = input("What is their role?")


if __name__ == '__main__':
    print("Welcome to MST's Valorant DBMS")
    while(user_choice != "quit" and user_choice != "q"):
        user_choice = main_menu()