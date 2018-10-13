import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    cur.execute("CREATE TABLE TEAM (team_id INT, team_name TEXT, PRIMARY KEY (team_id)) ;")
    cur.execute("CREATE TABLE MATCH (match_id INT, season_year INT, team1 INT, team2 INT, battedfirst INT,\
                battedsecond INT, venue_name TEXT, city_name TEXT, country_name TEXT, toss_winner TEXT,\
                match_winner TEXT,\
                toss_name TEXT, win_type TEXT, man_of_match TEXT, win_margin INT,\
                PRIMARY KEY (match_id), FOREIGN KEY (team1) REFERENCES TEAM(team_id),\
                FOREIGN KEY (team2) REFERENCES TEAM(team_id), FOREIGN KEY (battedfirst) REFERENCES TEAM(team_id) \
                FOREIGN KEY (battedsecond) REFERENCES TEAM(team_id) \
                )  ;")

    cur.execute("CREATE TABLE PLAYER (player_id INT,player_name TEXT,dob TIMESTAMP,batting_hand TEXT,\
                 bowling_skill TEXT, country_name TEXT,\
                  PRIMARY KEY (player_id)) ;")

    cur.execute("CREATE TABLE PLAYER_MATCH (playermatch_key BIGINT, match_id INT, player_id INT, batting_hand TEXT, \
                bowling_skill TEXT, role_desc TEXT, team_id INT, PRIMARY KEY (playermatch_key),\
                FOREIGN KEY(match_id) REFERENCES MATCH(match_id), \
                FOREIGN KEY(player_id) REFERENCES PLAYER(player_id)) ;")

    cur.execute("CREATE TABLE BALL_BY_BALL (match_id INT UNIQUE, innings_no INT UNIQUE, over_id INT UNIQUE, ball_id INT, \
                striker_batting_position INT, runs_scored INT, \
                extra_runs INT, out_type TEXT, striker INT, non_striker INT, bowler INT, \
                PRIMARY KEY (ball_id), \
                FOREIGN KEY (striker) REFERENCES PLAYER(player_id), \
                FOREIGN KEY (non_striker) REFERENCES PLAYER(player_id), \
                FOREIGN KEY (bowler) REFERENCES PLAYER(player_id) \
                 );")
    ipl.commit()
    ipl.close()