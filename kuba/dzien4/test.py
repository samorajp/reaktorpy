import pymysql

conn = pymysql.connect("localhost","root","Tubus1Tubus1", "skoczkowie")

c = conn.cursor()

c.execute("select * from skocznie")
print(c.fetchall())