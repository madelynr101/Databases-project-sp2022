create table game(
    Winning_Team               text     not null,
    Map                        text     not null,
    MST_final_score            integer  not null,
    Other_team_final_score     integer  not null,
    -- removed final score
    Tournament                 text,
    Num_games                  integer  not null,
    Game_num                   integer  primary key autoincrement not null
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
    Rounds_Survived integer not null,
    plays_for       text    not null,
    Agent           text    not null,
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

create table manager (
    m_name      text not null primary key,
    -- removed splitting up name to match manager
    manages     text not null,
    CONSTRAINT k_manager
        FOREIGN KEY (manages)
        REFERENCES manger(m_name)
);