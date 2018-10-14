import sqlite3
connection=sqlite3.connect("ipl.db")
crsr=connection.cursor()
crsr.execute("create table TEAM (team_id int primary key,team_name varchar(50));")
crsr.execute("create table PLAYER (player_id int primary key,player_name varchar(50)\
	,dob timestamp,batting_hand varchar(50),bowling_skill varchar(50),country_name varchar(50));")
crsr.execute("create table MATCH (match_id int primary key,season_year year,team1 int,team2 int,battedfirst int,battedsecond int,\
	venue_name varchar(50),city_name varchar(50),country_name varchar(50),toss_winner int,match_winner int\
	,toss_name varchar(50),win_type varchar(50),man_of_match int,win_margin int,\
	foreign key (team1) references TEAM(team_id),\
	foreign key (team2) references TEAM(team_id),\
	foreign key (battedfirst) references TEAM(team_id),\
	foreign key (battedsecond) references TEAM(team_id));")
crsr.execute("create table PLAYER_MATCH (playermatch_key bigint primary key,match_id int,player_id int,batting_hand varchar(50)\
	,bowling_skill varchar(50),role_desc varchar(50),team_id int,\
	foreign key (match_id) references MATCH(match_id),\
	foreign key (player_id) references TEAM(player_id),\
	foreign key (team_id) references TEAM(team_id));")
crsr.execute("create table BALL_BY_BALL (match_id int,innings_no int\
	,over_id int,ball_id int,striker_batting_position int,runs_scored int,extra_runs int,\
	out_type varchar(50),striker int,non_striker int,bowler int,\
	primary key (match_id,innings_no,over_id,ball_id),\
	foreign key (striker) references PLAYER(player_id),\
	foreign key (non_striker) references PLAYER(player_id),\
	foreign key (match_id) references MATCH(match_id));")

connection.commit()
connection.close()