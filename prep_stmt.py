query=input()
import sqlite3
conn=sqlite3.connect('ipl.db')
crsr=conn.cursor()
if query=='1':
	tid=input()
	tname=input()
	crsr.execute("insert into TEAM (team_id,team_name) values \
		(?,?);",(tid,tname))
elif query=='2':
	player_id=input()
	player_name=input()
	dob=input()
	batting_hand=input()
	bowling_skill=input()
	country_name=input()
	crsr.execute("insert into PLAYER (player_id\
		,player_name,dob,batting_hand,bowling_skill,\
		country_name) values (?,?,?,?,?,?);",(player_id\
			,player_name,dob,batting_hand,bowling_skill\
			,country_name))
elif query=='3':
	match_id=input()
	season_year=input()
	team1=input()
	team2=input()
	battedfirst=input()
	battedsecond=input()
	venue_name=input()
	city_name=input()
	country_name=input()
	toss_winner=input()
	match_winner=input()
	toss_name=input()
	win_type=input()
	man_of_match=input()
	win_margin=input()
	crsr.execute("insert into MATCH (match_id\
		,season_year,team1,team2,battedfirst,battedsecond\
		,venue_name,city_name,country_name,toss_winner\
		,match_winner,toss_name,win_type,man_of_match,\
		win_margin) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",\
		(match_id,season_year,team1,team2,battedfirst,battedsecond,\
		venue_name,city_name,country_name,toss_winner,match_winner,\
		toss_name,win_type,man_of_match,win_margin))
elif query=='4':
	playermatch_key=input()
	match_id=input()
	player_id=input()
	batting_hand=input()
	bowling_skill=input()
	role_desc=input()
	team_id=input()
	crsr.executemany("insert into PLAYER_MATCH (playermatch_key\
		,match_id,player_id,batting_hand,bowling_skill,role_desc\
		,team_id) values (?,?,?,?,?,?,?);",(playermatch_key,match_id\
			,player_id,batting_hand,bowling_skill,role_desc,team_id))
else:
	match_id=input()
	innings_no=input()
	over_id=input()
	ball_id=input()
	striker_batting_position=input()
	runs_scored=input()
	extra_runs=input()
	out_type=input()
	striker=input()
	non_striker=input()
	bowler=input()
	crsr.executemany("insert into BALL_BY_BALL\
	 (match_id,innings_no,over_id,ball_id,striker_batting_position\
	 ,runs_scored,extra_runs,out_type,striker,non_striker,bowler) values\
	 (?,?,?,?,?,?,?,?,?,?,?);",(match_id,innings_no,\
	 	over_id,ball_id,striker_batting_position,\
	 	runs_scored,extra_runs,out_type,striker,non_striker,bowler))
conn.commit()
conn.close()


