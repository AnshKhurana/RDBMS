import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    cur.execute("WITH cte AS \
                (SELECT player_id, player_name, AVG(B.res) ans \
                FROM PLAYER \
                JOIN (SELECT striker, match_id, COUNT(striker) res FROM BALL_BY_BALL GROUP BY striker, match_id) B \
                ON PLAYER.player_id = B.striker \
                GROUP BY player_id \
                ORDER BY CAST(ans as REAL) DESC) \
                SELECT *, \
                (SELECT AVG(ans) FROM cte c1 WHERE (9)=(SELECT COUNT(ans) FROM cte c2 WHERE c2.ans > c1.ans)) allow \
                FROM cte WHERE ans>=allow;")

    ipl.commit()
    for row in cur:
        print(str(row[0]) + "," + row[1] + "," + str(row[2]))
