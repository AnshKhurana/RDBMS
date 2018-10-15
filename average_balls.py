import sqlite3
conn=sqlite3.connect('ipl.db')
crsr=conn.cursor()
crsr.execute("select player_id,player_name,avg(rs) from\
	(select striker as st, count(runs_scored) as rs from\
	BALL_BY_BALL\
	group by match_id,striker)\
	,PLAYER where st=player_id\
	group by player_id	\
	order by avg(rs) desc;")
lcrsr=list(crsr)
for i in range(0,len(lcrsr)):
	if i>=10 and lcrsr[i][2]!=lcrsr[i-1][2]:
		break
	print('{},{},{}'.format(lcrsr[i][0],lcrsr[i][1],lcrsr[i][2]))
conn.commit()
conn.close()