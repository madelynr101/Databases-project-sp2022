# this is a databse 
import os, sys
import sqlite3
from getpass import getpass

import sql_functs

DB_FILE = "val.db"
PROMPT = "sus"

def clear_term():
    print(chr(27) + "[2J")

def main_menu():
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
    sys.exit(main()) 