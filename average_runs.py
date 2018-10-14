import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    c = ipl.cursor()

    c.execute("SELECT venue_name, SUM(runs_scored), COUNT(venue_name) FROM MATCH, BALL_BY_BALL \
              WHERE MATCH.match_id = BALL_BY_BALL.match_id \
                GROUP BY venue_name ORDER BY 2 DESC ;")
    for row in c:
        print(row)
    ipl.commit()
    ipl.close()
