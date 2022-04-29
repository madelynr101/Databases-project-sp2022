import os, sys
import sqlite3

from tabulate import tabulate

# Search for games based on certain maps
def games_by_map(db_file, map_name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
games[] = query all games with the same map_name
print(games[])

# Search for game that were won by certain teams
def games_won_by(db_file, team_name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
games[] = query all games won by team_name
print(games[])

# Search for games that were a part of certain tournaments
def tourna_games(db_file, tournament_name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
games[] = query all games with tournament_name
print(games[])
 
# In the searched games above be able to find rank 
def rank(db_file, game, IGN):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
query game for rank if they match IGN
print(rank)

# In the searched games above be able to find agent
def agent(db_file, game, IGN):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
query game for rank if they match IGN
print(agent)

# In the searched games above be able to find KDA
def KDA(db_file, game, IGN):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
query game for rank if they match IGN
print(KDA)

# In the searched games above be able to find role 
def role(db_file, game, IGN):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
query game for rank if they match IGN
print(role)

# In the searched games above be able to find RSV
def RSV(db_file, game, IGN):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "
query game for rank if they match IGN
print(RSV)

# look at last entry in database’s game number then print that number
def total_games(db_file): 
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select "

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