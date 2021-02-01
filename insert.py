import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='employe',user='root',password='test1234')

if conn.is_connected():
	print("connected to mysql db")

cursor=conn.cursor()
try:

        cursor.execute("insert into emp values(3,'john',101)")
        cursor.execute("insert into emp values(4,'smith',60000)")
        conn.commit()
        print("record is added")
except:
	conn.rollback()

    

cursor.close()
  
conn.close()