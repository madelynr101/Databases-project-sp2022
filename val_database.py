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
            i = int(input("Please enter the number of total rounds:\n" + PROMPT))
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
            c = input("Please enter player's rank in format 'rank_abbrevation''rank_number':\n" + PROMPT)
            d = input("Please enter player's team:\n" + PROMPT)
            e = input("Please enter player's role:\n" + PROMPT)
            f = int(input("Please enter player's kills:\n" + PROMPT))
            g = int(input("Please enter player's deaths minimum of 1:\n" + PROMPT))
            h = int(input("Please enter player's assists:\n" + PROMPT))
            i = (float(f)+float(h))/float(g)
            j = int(input("Please enter rounds played minimum of 1:\n" + PROMPT))
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
            sql_functs.tot_games(DB_FILE)
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
            sql_functs.view_all_games(DB_FILE)
            waitKey()
        #View games by game number
        if choice == '3':
            choice = "TBD"
            gno = int(input("Please enter the game number of the game you want to see:\n" + PROMPT))
            sql_functs.games_by_num(DB_FILE, gno)
            waitKey()
        #View games by MST Green/Gold
        if choice == '4':
            choice = "TBD"
            mst = input("Please enter the MST gold/green team to see their games:\n" + PROMPT)
            sql_functs.games_by_mst(DB_FILE, mst)
            waitKey()
        #View games by other team
        if choice == '5':
            choice = "TBD"
            team = input("Please enter the other team name to see their games:\n" + PROMPT)
            sql_functs.games_by_name(DB_FILE, team)
            waitKey()
        #View games by tournament
        if choice == '6':
            choice = "TBD"
            tourn = input("Please enter the tournament name to see those games:\n" + PROMPT)
            sql_functs.games_by_tourn(DB_FILE, tourn)
            waitKey()
        #View games by map
        if choice == '7':
            choice = "TBD"
            map = input("Please enter the map name to see games on that map:\n" + PROMPT)
            sql_functs.games_by_map(DB_FILE, map)
            waitKey()
        #View total number of games
        if choice == '8':
            choice = "TBD"
            sql_functs.tot_games(DB_FILE)
            waitKey()
        #View players in game number
        if choice == '9':
            choice = "TBD"
            gno = int(input("Please enter the game number of players you want to see:\n" + PROMPT))
            sql_functs.participates_by_num(DB_FILE, gno)
            waitKey()
        #Update game
        if choice == '10':
            choice = "TBD"
            
            update_choice = "TBD"
            continue_choice = 'yes'
            game_options = {
                '1': "The game's name.",
                '2': "The game's Winning Team.",
                '3': "The game's map.",
                '4': "The game's MST final score.",
                '5': "The game's other team final score.",
                '6': "The game's MST team name.",
                '7': "The game's other team name.",
                '8': "The game's tournament.",
                '9': "The game's number of rounds.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            }
            while(update_choice.lower() == 'yes'):
                print("What information about the game would you like to update?")
                for option, desc in game_options.items():
                    if option == 'b':
                        print('(b)ack' + ". " + desc)
                        continue
                    if option == 'q':
                        print('(q)uit' + ". " + desc)
                        continue
                    if option in ['back', 'quit']:
                        continue
                    print(option + ". " + desc)
                
                update_choice = input(PROMPT)
                gno = int(input("In which game? (insert game number):\n"+PROMPT))
                gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround = 0,0,0,0,0,0,0,0,0
                
                # Branching to account for specific changes 
                if update_choice == '1':
                    gname = input("Please enter a new game name:\n" + PROMPT)
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '2':
                    wteam = input("Please enter a new winning team:\n" + PROMPT)
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '3':
                    map = input("Please enter a new map name:\n" + PROMPT)
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '4':
                    mstfin = int(input("Please enter a new mst team final score:\n" + PROMPT))
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '5':
                    otherfin = int(input("Please enter a new other team final score:\n" + PROMPT))
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '6':
                    mst = input("Please enter a new mst team name:\n" + PROMPT)
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '7':
                    other = input("Please enter a new team name for the other team:\n" + PROMPT)
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '8':
                    tourn = input("Please enter a new tournament name:\n" + PROMPT)
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == '9':
                    numround = int(input("Please enter a new number of rounds:\n" + PROMPT))
                    sql_functs.update_game(DB_FILE,gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno)
                elif update_choice == 'b' or update_choice == 'back':
                    continue
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the game?(yes or no)\n" + PROMPT)
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
            sql_functs.view_all_players(DB_FILE)
            waitKey()
        #Update player
        if choice == '2':
            choice = "TBD"
            
            update_choice = "TBD"
            continue_choice = 'yes'
            player_options = {
                '1': "The player's in game name.",
                '2': "The player's in real life name.",
                '3': "The player's rank.",
                '4': "The player's team name.",
                '5': "The player's role.",
                '6': "The player's kills.",
                '7': "The player's deaths.",
                '8': "The player's assists.",
                '9': "The player's number of rounds survived.",
                '10': "The player's kda.",
                '11': "The player's kpr.",
                'b': "Go back.",
                'back': "",
                'q': "Quit.",
                'quit': "",
            }
            while(update_choice.lower() == 'yes'):
                print("What information about the player would you like to update?")
                for option, desc in player_options.items():
                    if option == 'b':
                        print('(b)ack' + ". " + desc)
                        continue
                    if option == 'q':
                        print('(q)uit' + ". " + desc)
                        continue
                    if option in ['back', 'quit']:
                        continue
                    print(option + ". " + desc)
                
                update_choice = input(PROMPT)
                ign = int(input("In which player? (insert their IGN):\n"+PROMPT))
                irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr = 0,0,0,0,0,0,0,0,0,0
                
                # Branching to account for specific changes 
                if update_choice == '1':
                    ign = input("Please enter a new in game name:\n" + PROMPT)
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '2':
                    irl = input("Please enter a new in real life name:\n" + PROMPT)
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '3':
                    rank = input("Please enter a new rank in format 'rank_abbrevation''rank_number':\n" + PROMPT)
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '4':
                    plays_for = input("Please enter a new team name:\n" + PROMPT)
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '5':
                    role = input("Please enter a new role name:\n" + PROMPT)
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '6':
                    kills = int(input("Please enter a new number of kills:\n" + PROMPT))
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '7':
                    deaths = int(input("Please enter a new number of deaths:\n" + PROMPT))
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '8':
                    assist = int(input("Please enter a new number of assists:\n" + PROMPT))
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '9':
                    rounds = int(input("Please enter a new number of rounds survived:\n" + PROMPT))
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '10':
                    kda = float(input("Please enter a new kda:\n" + PROMPT))
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == '11':
                    kpr = float(input("Please enter a new kpr:\n" + PROMPT))
                    sql_functs.update_player(DB_FILE,ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr)
                elif update_choice == 'b' or update_choice == 'back':
                    continue
                elif update_choice == 'q' or update_choice == 'quit':
                    exit()
                else:
                    print("Invalid input.")
                update_choice = input("Do you want to change any additional information about the player?(yes or no)\n" + PROMPT)
            waitKey()
        #View players who play for (team)
        if choice == '3':
            choice = "TBD"
            team = input("Please enter the team name who u want to see players for:\n" + PROMPT)
            sql_functs.play_for(DB_FILE, team)
            waitKey()
        #View players who play (role)
        if choice == '4':
            choice = "TBD"
            role = input("Please enter the team name who u want to see players for:\n" + PROMPT)
            sql_functs.plays_role(DB_FILE, role)
            waitKey()
        #View players with KDA over 1.5
        if choice == '5':
            choice = "TBD"
            sql_functs.kd_over(DB_FILE)
            waitKey()
        #View players with KDA under 1.5
        if choice == '6':
            choice = "TBD"
            sql_functs.kd_under(DB_FILE)
            waitKey()

def menu_teams():
    clear_term()
    choice = 'TBD'

    options = {
        '1': "View all teams",
        '2': "Update team",
        '3': "View manager of (team)",
        'q': "quit",
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
            sql_functs.view_all_teams(DB_FILE)
            waitKey()
        #Update team
        if choice == '2':
            choice = "TBD"
            update_choice = "TBD"
            continue_choice = 'yes'
            name = input("In which team? (insert team name):\n"+PROMPT)
            manag = 0
            update_choice = input("Please enter 1 to update team name 2 to update manager name:\n" + PROMPT)
            if update_choice == 1:
                name = input("You cannot change this with my current design but add a name to entice me")
                sql_functs.update_team(DB_FILE, name, manag)
            elif update_choice == 2:
                manag = input("Please enter the new name of the manager")
                sql_functs.update_team(DB_FILE, name, manag)
            else:
                print("Invalid input.")
            waitKey()
        #View manager of (team)
        if choice == '3':
            choice = "TBD"
            team = input("Please enter the team name who u want to see manager of:\n" + PROMPT)
            sql_functs.manager_of(DB_FILE, team)
            waitKey()


if __name__ == '__main__':
    print("Welcome to MST's Valorant DBMS")
    user_choice = "TBD"
    while(user_choice != "quit" and user_choice != "q"):
        user_choice = main_menu()