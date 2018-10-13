import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    cur.execute("SELECT venue_name, AVG( (SELECT SUM(runs_scored) FROM BALL_BY_BALL "
                "WHERE BALL_BY_BALL.match_id = MATCH.match_id)) as a "
                "FROM MATCH WHERE venue_name != 'NULL' "
                "GROUP BY venue_name "
                "ORDER BY a desc"
                )
    ipl.commit()
    for row in cur:
        print(row[0]+","+str(row[1]))
