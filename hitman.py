import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    cur.execute("SELECT player_id, player_name, C.sixes , C.balls, (C.sixes*1.0/C.balls) ans FROM PLAYER \
                JOIN (SELECT striker, COUNT(striker) balls, (SELECT COUNT(runs_scored) FROM BALL_BY_BALL b2 \
                WHERE b2.striker=b1.striker AND runs_scored=6) sixes FROM BALL_BY_BALL b1 GROUP BY striker) C\
                ON PLAYER.player_id = C.striker\
                GROUP BY player_id \
                ORDER BY ans DESC;")

    ipl.commit()
    for row in cur:
        print(str(row[0]) + "," + row[1] + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]))