import os, sys
import sqlite3

from tabulate import tabulate

# adds new row to the gmae table
def add_game(db_file, game): 
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into game (Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, MST_team, Other_team, Tournament, Num_rounds, Game_num) values (?,?,?,?,?,?,?,?,?,?);"
        curs.executemany(qry,game)

# adds new row to the player table
def add_player(db_file, player): 
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into player (IGN, IRL_name, Rank_is, Plays_for, Role_is, Kills, Deaths, Assists, KDA, Rounds_Played, KPR) values (?,?,?,?,?,?,?,?,?,?,?);"
        curs.executemany(qry,player)

# adds new row to the team table
def add_team(db_file, team): 
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into team (t_name, t_manager) values (?,?);"
        curs.executemany(qry,team)

#adds new row to the participates table
def add_participates(db_file, participates): 
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "insert into participates (p_name, game_no) values (?,?);"
        curs.executemany(qry,participates)

# View all games
def view_all_games(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, MST_team, Other_team, Tournament, Game_num from game"
        curs.execute(qry)
        headers = ["Game_name", "Winning_Team", "Map", "MST_final_score", "Other_team_final_score", "MST_team", "Other_team","Tournament", "Game_num"]
        print(tabulate(curs.fetchall(), headers))

# Search for game by game no
def games_by_num(db_file, gno):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, MST_team, Other_team,Tournament ,Game_num from game where Game_num = " + gno
        curs.execute(qry)
        headers = ["Game_name", "Winning_Team", "Map", "MST_final_score", "Other_team_final_score", "MST_team", "Other_team","Tournament","Game_num"]
        print(tabulate(curs.fetchall(), headers))

# Search for game by game MST
def games_by_mst(db_file, mst):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, MST_team, Other_team,Tournament ,Game_num from game where MST_team = " + mst
        curs.execute(qry)
        headers = ["Game_name", "Winning_Team", "Map", "MST_final_score", "Other_team_final_score", "MST_team", "Other_team","Tournament","Game_num"]
        print(tabulate(curs.fetchall(), headers))

# Search for game by game Other teams
def games_by_name(db_file, name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, MST_team, Other_team,Tournament ,Game_num from game where Other_team = " + name
        curs.execute(qry)
        headers = ["Game_name", "Winning_Team", "Map", "MST_final_score", "Other_team_final_score", "MST_team", "Other_team","Tournament","Game_num"]
        print(tabulate(curs.fetchall(), headers))

# Search for games that were a part of certain tournaments
def tourna_games(db_file, tournament_name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, MST_team, Other_team,Tournament, Game_num from game where Tournament = " + tournament_name
        curs.execute(qry)
        headers = ["Game_name", "Winning_Team", "Map", "MST_final_score", "Other_team_final_score", "MST_team", "Other_team","Tournament","Game_num"]
        print(tabulate(curs.fetchall(), headers))

# Search for game by map
def games_by_map(db_file, map):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select Game_name, Winning_Team, Map, MST_final_score, Other_team_final_score, MST_team, Other_team,Tournament ,Game_num from game where Map = " + map
        curs.execute(qry)
        headers = ["Game_name", "Winning_Team", "Map", "MST_final_score", "Other_team_final_score", "MST_team", "Other_team","Tournament","Game_num"]
        print(tabulate(curs.fetchall(), headers))

# use count to count number of rows in games table
def tot_games(db_file): 
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        s1 = "select COUNT(*) from game"
        curs.execute(s1)
        print()
        print("There are",curs.fetchall(), "current games in da database")
        print()

# view which players participate in a certain game number
def participates_by_num(db_file, gno):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select p_name, game_no from participates where game_no = " + gno
        curs.execute(qry)
        headers = ["p_name", "game_no"]
        print(tabulate(curs.fetchall(), headers))

#prints all players
def view_all_players(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select IGN, IRL_name, Rank_is, Plays_for, Role_is, Kills, Deaths, Assists, KDA, Rounds_Played, KPR from player"
        curs.execute(qry)
        headers = ["IGN", "IRL_name", "Rank_is", "Plays_for", "Role_is", "Kills", "Deaths", "Assists", "KDA", "Rounds_Played", "KPR"]
        print(tabulate(curs.fetchall(), headers))

#prints all players who play for team
def plays_for(db_file, team):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select IGN, IRL_name, Rank_is, Plays_for, Role_is, Kills, Deaths, Assists, KDA, Rounds_Played, KPR from player where Plays_for = " + team
        curs.execute(qry)
        headers = ["IGN", "IRL_name", "Rank_is", "Plays_for", "Role_is", "Kills", "Deaths", "Assists", "KDA", "Rounds_Played", "KPR"]
        print(tabulate(curs.fetchall(), headers))       

#prints all players who play certain role
def plays_role(db_file, role):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select IGN, IRL_name, Rank_is, Plays_for, Role_is, Kills, Deaths, Assists, KDA, Rounds_Played, KPR from player where Role_is = " + role
        curs.execute(qry)
        headers = ["IGN", "IRL_name", "Rank_is", "Plays_for", "Role_is", "Kills", "Deaths", "Assists", "KDA", "Rounds_Played", "KPR"]
        print(tabulate(curs.fetchall(), headers)) 

#prints all players who have kda under 1.5
def kd_under(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select IGN, IRL_name, Rank_is, Plays_for, Role_is, Kills, Deaths, Assists, KDA, Rounds_Played, KPR from player where KDA <= " + 1.5
        curs.execute(qry)
        headers = ["IGN", "IRL_name", "Rank_is", "Plays_for", "Role_is", "Kills", "Deaths", "Assists", "KDA", "Rounds_Played", "KPR"]
        print(tabulate(curs.fetchall(), headers))

#prints all players who have kda over 1.5
def kd_over(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select IGN, IRL_name, Rank_is, Plays_for, Role_is, Kills, Deaths, Assists, KDA, Rounds_Played, KPR from player where KDA >= " + 1.5
        curs.execute(qry)
        headers = ["IGN", "IRL_name", "Rank_is", "Plays_for", "Role_is", "Kills", "Deaths", "Assists", "KDA", "Rounds_Played", "KPR"]
        print(tabulate(curs.fetchall(), headers))

#prints all teams
def view_all_teams(db_file):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select t_name, t_manager from team"
        curs.execute(qry)
        headers = ["t_name", "t_manager"]
        print(tabulate(curs.fetchall(), headers))

#prints manager of team with team name
def manager_of(db_file, name):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        qry = "select t_name, t_manager from team where t_name = " + name
        curs.execute(qry)
        headers = ["t_name", "t_manager"]
        print(tabulate(curs.fetchall(), headers))

#updates manager of team cant update t_name with this setup
def update_team(db_file, name, manag):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        if name != 0:
            print("welp u cant change this so here is an egg O")
        elif manag != 0:
            qry = "update team set t_manager = \"" + manag + "\" where t_name = " + name
            curs.execute(qry)

#updates game
def update_game(db_file, gname,wteam,map,mstfin,otherfin,mst,other,tourn,numround,gno):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        if gname != 0:
            qry = "update game set Game_name = \"" + gname + "\" where Game_num = " + gno
            curs.execute(qry)
        elif wteam != 0:
            qry = "update game set Winnning_team = \"" + wteam + "\" where Game_num = " + gno
            curs.execute(qry)
        elif map != 0:
            qry = "update game set Map = \"" + map + "\" where Game_num = " + gno
            curs.execute(qry)
        elif mstfin != 0:
            qry = "update game set MST_final_score = \"" + mstfin + "\" where Game_num = " + gno
            curs.execute(qry)
        elif otherfin != 0:
            qry = "update game set Other_team_final_score = \"" + otherfin + "\" where Game_num = " + gno
            curs.execute(qry)
        elif mst != 0:
            qry = "update game set MST_team = \"" + mst + "\" where Game_num = " + gno
            curs.execute(qry)
        elif other != 0:
            qry = "update game set Other_team = \"" + other + "\" where Game_num = " + gno
            curs.execute(qry)
        elif tourn != 0:
            qry = "update game set Tournament = \"" + tourn + "\" where Game_num = " + gno
            curs.execute(qry)
        elif numround != 0:
            qry = "update game set Num_rounds = \"" + numround + "\" where Game_num = " + gno
            curs.execute(qry)


#updates player
def update_player(db_file, ign,irl,rank,plays_for,role,kills,deaths,assist,kda,rounds,kpr):
    with sqlite3.connect(db_file) as connector:
        curs = connector.cursor()
        if irl != 0:
            qry = "update player set IRL_name = \"" + irl + "\" where IGN = " + ign
            curs.execute(qry)
        elif rank != 0:
            qry = "update player set Rank_is = \"" + rank + "\" where IGN = " + ign
            curs.execute(qry)
        elif plays_for != 0:
            qry = "update player set Plays_for = \"" + plays_for + "\" where IGN = " + ign
            curs.execute(qry)
        elif role != 0:
            qry = "update player set Role_is = \"" + role + "\" where IGN = " + ign
            curs.execute(qry)
        elif kills != 0:
            qry = "update player set Kills = \"" + kills + "\" where IGN = " + ign
            curs.execute(qry)
        elif deaths != 0:
            qry = "update player set Deaths = \"" + deaths + "\" where IGN = " + ign
            curs.execute(qry)
        elif assist != 0:
            qry = "update player set Assist = \"" + assist + "\" where IGN = " + ign
            curs.execute(qry)
        elif rounds != 0:
            qry = "update player set Num_rounds = \"" + rounds + "\" where IGN = " + ign
            curs.execute(qry)
        elif kda != 0:
            qry = "update player set KDA = \"" + kda + "\" where IGN = " + ign
            curs.execute(qry)
        elif kpr != 0:
            qry = "update player set KPR = \"" + kpr + "\" where IGN = " + ign
            curs.execute(qry)

db_file = "val.db"
schema_file = "create_tables.sql"

db_exists = os.path.exists(db_file) # Checks to see if a database file already exists.

if not db_exists: # Creates a new database file with the schema read from the sql file if there isn't already a database file.
    with sqlite3.connect(db_file) as connector:
        with open(schema_file, 'rt') as f:
            schema = f.read()
        print(schema)
        connector.executescript(schema)

if __name__ == "__main__":
     pass