import sqlite3, csv

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    with open('team.csv', 'r') as fin:
        dr = list(csv.reader(fin))
        dicts = ({'team_id': line[0], 'team_name': line[1]} for line in dr[1:])
        to_db = ((i['team_id'], i['team_name']) for i in dicts)
        for a in to_db:
            print(a)
        cur.executemany("INSERT INTO TEAM (team_id, team_name)  VALUES (?, ?);", to_db)
    ipl.commit()
    # player_id,player_name,dob,batting_hand,bowling_skill,country_name
    with open('player.csv', 'r') as fin:
        dr = list(csv.reader(fin))
        dicts = ({'player_id': line[0], 'player_name': line[1], 'dob': line[2], 'batting_hand': line[3],
                  'bowling_skill': line[4], 'country_name': line[5]} for line in dr[1:])
        to_db = ((i['player_id'], i['player_name'], i['dob'], i['batting_hand'], i['bowling_skill'], i['country_name'])
                 for i in dicts)
        for a in to_db:
            print(to_db)
        cur.executemany("INSERT INTO PLAYER (player_id, player_name, dob, batting_hand, bowling_skill, country_name)\
         VALUES (?, ?, ?, ?, ?, ?);", to_db)
    ipl.commit()

    # playermatch_key,match_id,player_id,batting_hand,bowling_skill,role_desc,team_id
    with open('player_match.csv', 'r') as fin:
        dr = list(csv.reader(fin))
        dicts = ({'playermatch_key': line[0], 'match_id': line[1], 'player_id': line[2], 'batting_hand': line[3],
                  'bowling_skill': line[4], 'role_desc': line[5], 'team_id': line[6]} for line in dr[1:])
        to_db = ((i['playermatch_key'], i['match_id'], i['player_id'], i['batting_hand'], i['bowling_skill'],
                  i['role_desc'], i['team_id']) \
                 for i in dicts)
        for a in to_db:
            print(to_db)
        cur.executemany("INSERT INTO PLAYER_MATCH ( playermatch_key,match_id,player_id,batting_hand,bowling_skill,role_desc,team_id)\
         VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    ipl.commit()

    with open('ball_by_ball.csv', 'r') as fin:
        dr = list(csv.reader(fin))
        dicts = ({'match_id': line[0], 'innings_no': line[1], 'over_id': line[2], 'ball_id': line[3],
                  'striker_batting_position': line[4], 'runs_scored': line[5], 'extra_runs': line[6], 'out_type': line[7],
                  'striker': line[8], 'non_striker': line[9], 'bowler': line[10]
                  } for line in dr[1:])
        to_db = ((i['match_id'], i['innings_no'], i['over_id'], i['ball_id'], i['striker_batting_position'],
                  i['runs_scored'], i['extra_runs'], i['out_type'], i['striker'], i['non_striker'], i['bowler']) for i
                 in dicts)
        for a in to_db:
            print(a)
        cur.executemany("INSERT INTO BALL_BY_BALL (match_id,innings_no,over_id,ball_id,striker_batting_position, \
                        runs_scored,extra_runs,out_type,striker,non_striker,bowler)\
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    ipl.commit()

    with open('match.csv', 'r') as fin:
        dr = list(csv.reader(fin))
        dicts = ({'match_id': line[0], 'season_year': line[1], 'team1': line[2], 'team2': line[3],
                  'battedfirst': line[4], 'battedsecond': line[5], 'venue_name': line[6], 'city_name': line[7],
                  'country_name': line[8], 'toss_winner': line[9], 'match_winner': line[10], 'toss_name': line[11],
                  'win_type': line[12], 'man_of_match': line[13], 'win_margin': line[14],
                  } for line in dr[1:])
        to_db = ((i['match_id'], i['season_year'], i['team1'], i['team2'], i['battedfirst'], i['battedsecond'],
                  i['venue_name'], i['city_name'], i['country_name'], i['toss_winner'], i['match_winner'],
                  i['toss_name'],
                  i['win_type'], i['man_of_match'], i['win_margin']
                  ) for i in dicts)
        for a in to_db:
            print(a)
        cur.executemany("INSERT INTO MATCH (match_id,season_year,team1,team2,battedfirst,battedsecond,venue_name,city_name,\
            country_name,toss_winner,match_winner,toss_name,win_type,man_of_match,win_margin)\
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    ipl.commit()
