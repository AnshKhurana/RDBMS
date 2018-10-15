import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    params = []
    q = input()

    if q == '1':
        for x in range(2):
            params.append(input())
        cur.execute("INSERT INTO TEAM (team_id, team_name) VALUES (?, ?);", params)

    elif q == '3':
        for x in range(15):
            params.append(input())
        cur.executemany("INSERT INTO MATCH (match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name,\
                                 city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match,\
                                 win_margin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", params)

    elif q == '2':
        for x in range(6):
            params.append(input())
        cur.executemany("INSERT INTO PLAYER (player_id,player_name,dob,batting_hand,bowling_skill,country_name)\
                                 VALUES (?, ?, ?, ?, ?, ?);", params)

    elif q == '4':
        for x in range(7):
            params.append(input())
        cur.executemany("INSERT INTO PLAYER_MATCH (playermatch_key,match_id,player_id,batting_hand,bowling_skill,role_desc,\
                                    team_id) VALUES (?, ?, ?, ?, ?, ?, ?);", params)

    elif q == '5':
        for x in range(11):
            params.append(input())
        cur.executemany("INSERT INTO BALL_BY_BALL (match_id,innings_no,over_id,ball_id,striker_batting_position,\
                                runs_scored,extra_runs,out_type,striker,non_striker,bowler)\
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", params)

    ipl.commit()
    ipl.close()