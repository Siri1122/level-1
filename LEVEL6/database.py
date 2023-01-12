import sqlite3
connect = sqlite3.connect("c://sqlite//hcl1.db")
cur=connect.cursor()
# sql=""" insert into filelog values(?,?);"""
# data=(100,'d://jose1//demo.txt')
# cur.execute(sql,data)
# connect.commit()
cur.execute("select * from filelog ")
rows=cur.fetchall()
for r in rows:
    print(r)
