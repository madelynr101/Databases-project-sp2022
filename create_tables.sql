
create table team(
    t_name      varchar(255) not null primary key,
    t_manager   text not null
);

create table game(
    Game_name                  text     not null,
    Winning_Team               text     not null,
    Map                        text     not null,
    MST_final_score            integer  not null,
    Other_team_final_score     integer  not null,
    -- removed final score
    MST_team                   text     not null REFERENCES team(t_name),
    Other_team                 text     not null REFERENCES team(t_name),
    Tournament                 text,
    Num_rounds                 integer  not null,
    Game_num                   integer  primary key autoincrement
);

create table player(
    IGN             varchar(255)    not null primary key,
    IRL_name        text    not null,
    Rank_is         text    not null,
    Plays_for       text    not null REFERENCES team(t_name),
    Role_is         text    not null,
    Kills           integer not null,
    Deaths          integer not null,
    Assists         integer not null,
    KDA             float   not null,
    Rounds_Played   integer not null,
    KPR             float   not null
);

create table participates(
    p_name      text not null REFERENCES player(IGN),
    game_no     text not null REFERENCES game(Game_num),
    CONSTRAINT k_p1
        PRIMARY KEY (p_name, game_no)
);