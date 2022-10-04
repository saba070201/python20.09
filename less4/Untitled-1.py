import sqlite3

id = int(input("id: "))
name = input("name: ")
email = input("email: ")

con = sqlite3.connect("C:/Users/Admin/Documents/Veselkov/testtete.db")
cur = con.cursor()
#select_query = '''CREATE TABLE My_db_table ('id' primary key , 'name' text(100), 'email' text(90))'''
insert_query = f''' INSERT INTO My_db_table VALUES('{id}','{name}','{email}') '''
#select_query = '''select * from My_db_table '''
cur.execute(insert_query)
#res = cur.fetchall()
con.commit()

#for i in res:
#  print(i)
#  if i[1] == "Oleg":
#    print("это олег")
#  else:
#    print("это не олег")

