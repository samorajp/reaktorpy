import pymysql

conn = pymysql.connect("localhost", "root", "03041983pawel", "skoczkowie")

c= conn.cursor()
c.execute("select * from kibice")
print(c.fetchall())

c.execute("select * from skocznie")
print(c.fetchall())