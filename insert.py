import sqlite3,csv
conn=sqlite3.connect("ipl.db")
crsr=conn.cursor()
with open('team.csv') as fhand:
	dr=list(csv.DictReader(fhand))
	to_db=[(i['team_id'],i['team_name']) for i in dr]
	crsr.executemany("insert into TEAM (team_id,team_name)\
	 values (?,?);",to_db)
with open('player.csv') as fhand:
	dr=csv.DictReader(fhand)
	to_db=[(i['player_id'],i['player_name'],\
		i['dob'],i['batting_hand'],i['bowling_skill'],\
		i['country_name']) for i in dr]
	# print(to_db)
	crsr.executemany("insert into PLAYER (player_id\
		,player_name,dob,batting_hand,bowling_skill,\
		country_name) values (?,?,?,?,?,?);",to_db)

with open('player_match.csv') as fhand:
	dr=csv.DictReader(fhand)
	to_db=[(i['playermatch_key'],i['match_id']\
	,i['player_id'],i['batting_hand'],i['bowling_skill'],\
	i['role_desc'],i['team_id']) for i in dr]
	crsr.executemany("insert into PLAYER_MATCH (playermatch_key\
		,match_id,player_id,batting_hand,bowling_skill,role_desc\
		,team_id) values (?,?,?,?,?,?,?);",to_db)
with open('match.csv') as fhand:
	dr=csv.DictReader(fhand)
	to_db=[(i['match_id'],i['season_year'],i['team1'],i['team2']\
		,i['battedfirst'],i['battedsecond'],i['venue_name']\
		,i['city_name'],i['country_name'],i['toss_winner']\
		,i['match_winner'],i['toss_name'],i['win_type']\
		,i['man_of_match'],i['win_margin']) for i in dr]
	crsr.executemany("insert into MATCH (match_id\
		,season_year,team1,team2,battedfirst,battedsecond\
		,venue_name,city_name,country_name,toss_winner\
		,match_winner,toss_name,win_type,man_of_match,\
		win_margin) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",to_db)
with open('ball_by_ball.csv') as fhand:
	dr=csv.DictReader(fhand)
	to_db=[(i['match_id'],i['innings_no'],i['over_id'],i['ball_id']\
		,i['striker_batting_position'],i['runs_scored'],\
		i['extra_runs'],i['out_type'],i['striker'],i['non_striker'],\
		i['bowler']) for i in dr]
	crsr.executemany("insert into BALL_BY_BALL\
	 (match_id,innings_no,over_id,ball_id,striker_batting_position\
	 ,runs_scored,extra_runs,out_type,striker,non_striker,bowler) values\
	 (?,?,?,?,?,?,?,?,?,?,?);",to_db)

conn.commit()
conn.close()

