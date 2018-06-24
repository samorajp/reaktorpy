import pymysql

conn = pymysql.connect("localhost", "root", "waszehaslodoroota", "skoczkowie")

c = conn.cursor()

c.execute("select * from kibice")

print(c.fetchall())