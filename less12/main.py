# import sqlite3
# from unittest import result
# conn=sqlite3.connect('less12/data/test.db')
# cur=conn.cursor()
# # cur.execute("""CREATE TABLE IF NOT EXISTS users(
# #     ID INTEGER NOT NULL UNIQUE,
# #     login TEXT NOT NULL UNIQUE,
# #     password TEXT NOT NULL,
# #     PRIMARY KEY("ID" AUTOINCREMENT) 
# # );""")
# # cur.execute(" SELECT ID,login FROM users WHERE ID=1 OR ID=3; ")
# # results=cur.fetchall()
# # print(results)
# # simpleuser=('anna','anna123')
# # cur.execute("INSERT INTO users(login,password) VALUES(?,?);",simpleuser)
# cur.execute("DELETE  FROM users;")
# conn.commit()
# conn.close()
import sqlite3
import hashlib 
conn=sqlite3.connect('less12/data/test.db')
cur=conn.cursor()
log='misha'
pas='misha123'
hashed_log=hashlib.sha256(log.encode()).hexdigest()
hashed_pas=hashlib.sha256(pas.encode()).hexdigest()
data=(hashed_log,hashed_pas)
cur.execute("INSERT INTO users(login,password) VALUES(?,?);",data)
conn.commit()
conn.close()


