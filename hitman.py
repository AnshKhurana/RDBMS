import sqlite3
conn=sqlite3.connect('ipl.db')
crsr=conn.cursor()
crsr.execute("select a,b,count(c),d, count(c)*1.0/d from (select a as a,b as b,c as c,d as d from (select pid as a,player_name as b,\
 runs_scored as c, crs as d\
 from (select striker as pid\
	, count(runs_scored) as crs\
 from BALL_BY_BALL group by striker),BALL_BY_BALL\
 inner join PLAYER on PLAYER.player_id=BALL_BY_BALL.striker \
 where pid=PLAYER.player_id) \
 where c=6) \
 group by a \
 order by count(c)*1.0/d desc;")
for i in crsr:
	print('{},{},{},{},{}'.format(i[0],i[1],i[2],i[3],i[4]))
conn.commit()
conn.close()