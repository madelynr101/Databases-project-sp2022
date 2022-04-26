create table game(
    Winning_Team               text not null,
    Map                        text not null,
    MST_final_score            integer not null,
    Other_team_final_score     integer not null,
    Final_score                integer not null,
    Tournament                 text,
    Num_games                  integer not null,
    Game_num                   integer primary key autoincrement not null,
);

create table player(
    IGN             text not null primary key,
    IRL_name        text not null,
    Rank_is         text not null,
    Role_is         text not null,
    KPR             integer not null,
    Kills           integer not null,
    Deaths          integer not null,
    Assists         integer not null,
    Rounds_Survived text not null,
);

create table team(
    t_name      text not null primary key,
    t_manager   text not null REFERENCES manager(m_name),
    player1     text not null REFERENCES player(IGN),
    player2     text not null REFERENCES player(IGN),
    player3     text not null REFERENCES player(IGN),
    player4     text not null REFERENCES player(IGN),
    player5     text not null REFERENCES player(IGN),
    
    CONSTRAINT k_caretaker
        FOREIGN KEY (eid)
        REFERENCES employee(eid)
);

create table manager (
    zoo_subsection text not null,
    eid integer    integer not null,
    CONSTRAINT k_manager
        FOREIGN KEY (eid)
        REFERENCES employee(eid)
);


