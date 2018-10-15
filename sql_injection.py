import sqlite3

if __name__ == '__main__':
    ipl = sqlite3.connect('ipl.db')
    cur = ipl.cursor()
    arg1 = input()
    arg2 = input()
    arg3 = input()

    if arg1 == '1' and arg2 == '0':
        cur.execute("DELETE FROM TEAM WHERE team_name = " + arg3)

    elif arg1 == '1' and arg2 == '1':
        cur.execute("DELETE FROM TEAM WHERE team_name = ?", [arg3])

    elif arg1 == '2' and arg2 == '0':
        cur.execute("DELETE FROM PLAYER WHERE player_name = " + arg3)

    elif arg1 == '2' and arg2 == '1':
        cur.execute("DELETE FROM PLAYER WHERE player_name = ?", [arg3])

    elif arg1 == '3' and arg2 == '0':
        cur.execute("DELETE FROM MATCH WHERE match_id = " + arg3)

    elif arg1 == '3' and arg2 == '1':
        cur.execute("DELETE FROM MATCH WHERE match_id = ?", [arg3])

    ipl.commit()
    ipl.close()