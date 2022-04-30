import os, sys
import sqlite3

from tabulate import tabulate

# View all games
def view_all_games(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, Game_num from game"
        curs.execute(qry)
        headers = ["Game_name", "Winning_Team", "Map", "MST_final_score", "Other_team_final_score", "Game_num"]
        print(tabulate(curs.fetchall(), headers))

# Search for game that were won by certain teams
def games_won_by(db_file, team_name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "

# Search for games that were a part of certain tournaments
def tourna_games(db_file, tournament_name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "

# use count to count number of rowsin games table
def tot_games(db_file): 
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select COUNT(*) from game"
        curs.execute(s1)

db_file = "val.db"
schema_file = "create_table.sql"

db_exists = os.path.exists(db_file) # Checks to see if a database file already exists.

if not db_exists: # Creates a new database file with the schema read from the sql file if there isn't already a database file.
    with sqlite3.connect(db_file) as connector:
        with open(schema_file, 'rt') as f:
            schema = f.read()
        connector.executescript(schema)

if __name__ == "__main__":
     pass