import sqlite3
conn=sqlite3.connect('ipl.db')
crsr=conn.cursor()
sobj=crsr.execute("select vn,avg(rs) from (select venue_name as vn, sum(runs_scored) as rs from\
	BALL_BY_BALL\
	inner join MATCH on BALL_BY_BALL.match_id=MATCH.match_id\
	group by BALL_BY_BALL.match_id)\
	group by vn\
	order by avg(rs) desc;")
for i in sobj:
	print(i[0],i[1])
conn.commit()
conn.close()