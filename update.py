import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='customers',user='root',password='test1234')

if conn.is_connected():
	print("connected to mysql db")

cursor=conn.cursor()
try:

        cursor.execute("insert into emp values (1,'john',20000)")
        cursor.execute("insert into emp(2,'geetha','8248')")
        cursor.execute("insert into emp values(4,'vidya','8248')")
   
        conn.commit()
        print("record is added")
except:
	conn.rollback()

    

cursor.close()
  
conn.close()