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
        'q': "quit",
        'quit': "quit",
    }

    while(choice != 'q' and choice != 'quit'):
        clear_term()
        print("Please choose from the options below: ")
        for option, desc in options.items():
            print(option + ". " + desc)
        choice = input(PROMPT)

        if choice not in options.keys():
            print("Invalid choice. Choose from the options below:")
            continue 

        # Add game
        if choice == '1':
            choice = "TBD"
            game = []
            a = input("Please enter game name:\n" + PROMPT)
            b = input("Please enter winning team:\n" + PROMPT)                
            c = input("Please enter map:\n" + PROMPT)
            d = int(input("Please enter mst team's final score:\n" + PROMPT))
            e = int(input("Please enter other team's final score:\n" + PROMPT))
            f = input("Please enter if it was Green/Gold mst team:\n" + PROMPT)
            g = input("Please enter other team's name:\n" + PROMPT)
            h = input("Please enter Tournament name (if there was one):\n" + PROMPT)
            i = int(input("Please enter the number of total games:\n" + PROMPT))
            j = int(input("Please enter unique game number:\n" + PROMPT))
            game.append([a,b,c,d,e,f,g,h,i,j])
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
            player = []
            a = input("Please enter IGN:\n" + PROMPT)
            b = input("Please enter player's irl name:\n" + PROMPT)                
            c = input("Please enter player's rank:\n" + PROMPT)
            d = input("Please enter player's team:\n" + PROMPT)
            e = input("Please enter player's role:\n" + PROMPT)
            f = int(input("Please enter unique player's kills:\n" + PROMPT))
            g = int(input("Please enter unique player's deaths:\n" + PROMPT))
            h = int(input("Please enter unique player's assists:\n" + PROMPT))
            i = (float(f)+float(h))/float(g)
            j = int(input("Please enter rounds played:\n" + PROMPT))
            k = float(g)/float(j)
            player.append([a,b,c,d,e,f,g,h,i,j,k])
            sql_functs.add_player(DB_FILE, player)  
            waitKey()
        # View/Update Player
        elif choice == '4':
            choice = "TBD"
            menu_players()
            waitKey()
        # Add Team
        elif choice == '5':
            choice = "TBD"
            team = []
            a = input("Please enter team name:\n" + PROMPT)
            b = input("Please enter team's manager:\n" + PROMPT)                
            team.append([a,b])
            sql_functs.add_team(DB_FILE, team)  
            waitKey()
        # View/Update teams
        elif choice == '6':
            choice = "TBD"
            menu_teams()
            waitKey()
        # View num games
        elif choice == '7':
            choice = "TBD"
            sql_functs.num_games(DB_FILE)
            waitKey()
    return choice


def menu_games():
    clear_term()
    choice = 'TBD'

    options = {
        '1': "Add players to game",
        '2': "View all games",
        '3': "View games by game number",
        '4': "View games by MST Green/Gold",
        '5': "View games by other team",
        '6': "View games by tournament",
        '7': "View games by map",
        '8': "View total number of games",
        '9': "View players in game number",
        '10': "Update game",
        'q': "quit",
        'quit': "quit",
    }

    while(choice != 'q' and choice != 'quit'):
        clear_term()
        print("Please choose from the options below: ")
        for option, desc in options.items():
            print(option + ". " + desc)
        choice = input(PROMPT)

        if choice not in options.keys():
            print("Invalid choice. Choose from the options below:")
            continue 
        
        #Add players to game
        if choice == '1':
            choice = "TBD"
            participates = []
            a = input("Please enter player ign:\n" + PROMPT)
            b = input("Please enter game number:\n" + PROMPT)                
            participates.append([a,b])
            sql_functs.add_participates(DB_FILE, participates)  
            waitKey()
        #View all games
        if choice == '2':
            choice = "TBD"
            waitKey()
        #View games by game number
        if choice == '3':
            choice = "TBD"
            waitKey()
        #View games by MST Green/Gold
        if choice == '4':
            choice = "TBD"
            waitKey()
        #View games by other team
        if choice == '5':
            choice = "TBD"
            waitKey()
        #View games by tournament
        if choice == '6':
            choice = "TBD"
            waitKey()
        #View games by map
        if choice == '7':
            choice = "TBD"
            waitKey()
        #View total number of games
        if choice == '8':
            choice = "TBD"
            waitKey()
        #View players in game number
        if choice == '9':
            choice = "TBD"
            waitKey()
        #Update game
        if choice == '10':
            choice = "TBD"
            waitKey()

def menu_players():
    clear_term()
    choice = 'TBD'

    options = {
        '1': "View all players",
        '2': "Update player",
        '3': "View players who play for (team)",
        '4': "View players who play (role)",
        '5': "View players who have KDA over 1.5",
        '6': "View players who have KDA under 1.5",
        'q': "quit",
        'quit': "quit",
    }

    while(choice != 'q' and choice != 'quit'):
        clear_term()
        print("Please choose from the options below: ")
        for option, desc in options.items():
            print(option + ". " + desc)
        choice = input(PROMPT)

        if choice not in options.keys():
            print("Invalid choice. Choose from the options below:")
            continue 
        
        #View all players
        if choice == '1':
            choice = "TBD"  
            waitKey()
        #Update player
        if choice == '2':
            choice = "TBD"
            waitKey()
        #View players who play for (team)
        if choice == '3':
            choice = "TBD"
            waitKey()
        #View players who play (role)
        if choice == '4':
            choice = "TBD"
            waitKey()
        #View players with KDA over 1.5
        if choice == '5':
            choice = "TBD"
            waitKey()
        #View players with KDA under 1.5
        if choice == '6':
            choice = "TBD"
            waitKey()

def menu_teams():
    clear_term()
    choice = 'TBD'

    options = {
        '1': "View all teams",
        '2': "Update team",
        '3': "View manager of (team)",
        'q': "quit",
        'quit': "quit",
    }

    while(choice != 'q' and choice != 'quit'):
        clear_term()
        print("Please choose from the options below: ")
        for option, desc in options.items():
            print(option + ". " + desc)
        choice = input(PROMPT)

        if choice not in options.keys():
            print("Invalid choice. Choose from the options below:")
            continue 
        
        #View all teams
        if choice == '1':
            choice = "TBD"  
            waitKey()
        #Update team
        if choice == '2':
            choice = "TBD"
            waitKey()
        #View manager of (team)
        if choice == '3':
            choice = "TBD"
            waitKey()


if __name__ == '__main__':
    print("Welcome to MST's Valorant DBMS")
    while(user_choice != "quit" and user_choice != "q"):
        user_choice = main_menu()