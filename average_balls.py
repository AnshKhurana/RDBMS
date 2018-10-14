
import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    cur.execute("SELECT player_id, player_name, AVG(B.res) ans FROM PLAYER \
                JOIN (SELECT striker, match_id, COUNT(striker) res FROM BALL_BY_BALL GROUP BY striker, match_id) B \
                ON PLAYER.player_id = B.striker \
                GROUP BY player_id \
                ORDER BY CAST( ans as REAL) DESC ;")

    ipl.commit()
    for row in cur:
        print(str(row[0]) + "," + row[1] + "," + str(row[2])) 