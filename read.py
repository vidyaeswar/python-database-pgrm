import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='employe',user='root',password='test1234')

if conn.is_connected():
	print("connected to mysql db")

cursor=conn.cursor()

cursor.execute('select* from emp')

row=cursor.fetchall()

while row is not None:

    print(row)
    row=cursor.fetchone()

cursor.close()
  
conn.close()