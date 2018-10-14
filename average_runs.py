import sqlite3
conn=sqlite3.connect("ipl.db")
csr=conn.cursor()
csr2=conn.cursor()
staddic={}
for i in csr.execute("select\
 match_id,runs_scored,extra_runs from BALL_BY_BALL"):
 mid=i[0]
 mrun=i[1]+i[2]
 stadname=csr2.execute("select distinct venue_name\
  from MATCH where match_id="+str(mid))
 # print('yo')
 sname=list(stadname)[0][0]
 staddic[sname]=\
 staddic.get(sname,0)
 if(staddic[sname]==0):
 	st=set()
 	st.add(mid)
 	# print(staddic[sname],set(mid))
 	staddic[sname]=[mrun,st]
 else:
 	staddic[sname][0]+=mrun
 	staddic[sname][1].add(mid)
for e in staddic:
	staddic[e]=staddic[e][0]/len(staddic[e][1])
# print(staddic)
staddic=list(staddic.items())
# print(staddic)
staddic.sort(key=lambda x:x[1],reverse=True)
# print(staddic)
for i in staddic:
	print("{}, {}".format(i[0],i[1]))
conn.commit()
conn.close()