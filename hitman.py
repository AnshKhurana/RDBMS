import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    cur.execute("SELECT player_id, player_name, B.sixes , C.balls, (B.sixes*1.0/C.balls) ans FROM PLAYER \
                JOIN (SELECT striker, COUNT(runs_scored) sixes \
                FROM BALL_BY_BALL WHERE runs_scored = 6 GROUP BY striker HAVING sixes > 0) B \
                ON PLAYER.player_id = B.striker \
                JOIN (SELECT striker, COUNT(striker) balls FROM BALL_BY_BALL GROUP BY striker) C\
                ON PLAYER.player_id = C.striker\
                GROUP BY player_id \
                ORDER BY ans DESC;")

    ipl.commit()
    for row in cur:
        print(str(row[0]) + "," + row[1] + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]))