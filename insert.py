import csv
import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    with open('team.csv', 'r') as fin:
        dr = list(csv.reader(fin))

        cur.executemany("INSERT INTO TEAM (team_id, team_name) VALUES (?, ?);", dr[1:])
    ipl.commit()

    with open('match.csv', 'r') as fin:
        dr = list(csv.reader(fin))

        cur.executemany("INSERT INTO MATCH (match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name,\
                         city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match,\
                         win_margin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", dr[1:])
    ipl.commit()

    with open('player.csv', 'r') as fin:
        dr = list(csv.reader(fin))

        cur.executemany("INSERT INTO PLAYER (player_id,player_name,dob,batting_hand,bowling_skill,country_name)\
                         VALUES (?, ?, ?, ?, ?, ?);", dr[1:])
    ipl.commit()

    with open('player_match.csv', 'r') as fin:
        dr = list(csv.reader(fin))

        cur.executemany("INSERT INTO PLAYER_MATCH (playermatch_key,match_id,player_id,batting_hand,bowling_skill,role_desc,\
                        team_id) VALUES (?, ?, ?, ?, ?, ?, ?);", dr[1:])
    ipl.commit()

    with open('ball_by_ball.csv', 'r') as fin:
        dr = list(csv.reader(fin))

        cur.executemany("INSERT INTO BALL_BY_BALL (match_id,innings_no,over_id,ball_id,striker_batting_position,\
                        runs_scored,extra_runs,out_type,striker,non_striker,bowler)\
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", dr[1:])
    ipl.commit()
