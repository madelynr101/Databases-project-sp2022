create table game(
    Game_name                  text     not null,
    Winning_Team               text     not null,
    Map                        text     not null,
    MST_final_score            integer  not null,
    Other_team_final_score     integer  not null,
    -- removed final score
    MST_team                   text     not null,
    Other_team                 text     not null,
    Tournament                 text,
    Num_rounds                 integer  not null,
    Game_num                   integer  primary key autoincrement
    CONSTRAINT k_game1
        FOREIGN KEY (MST_team)
        REFERENCES team(t_name),
    CONSTRAINT k_game2
        FOREIGN KEY (Other_team)
        REFERENCES team(t_name),
);

create table player(
    IGN             text    not null primary key,
    IRL_name        text    not null,
    Rank_is         text    not null,
    Role_is         text    not null,
    KPR             float   not null,
    Kills           integer not null,
    Deaths          integer not null,
    Assists         integer not null,
    KDA             float   not null,
    Rounds_Played   integer not null,
    plays_for       text    not null,
    CONSTRAINT k_player
        FOREIGN KEY (plays_for)
        REFERENCES team(t_name),
);

create table team(
    t_name      text not null primary key,
    t_manager   text not null,
    CONSTRAINT k_team
        FOREIGN KEY (t_manager)
        REFERENCES manager(m_name)
);

create table participates(
    p_name      text not null,
    game_no     text not null,
    CONSTRAINT k_p1
        PRIMARY KEY (p_name, game_no)
    CONSTRAINT k_p2
        FOREIGN KEY (p_name)
        REFERENCES player(IGN)
    CONSTRAINT k_p3
        FOREIGN KEY (game_no)
        REFERENCES game(Game_num)

create table manager (
    m_name      text not null primary key,
    --removed splitting first and last
);