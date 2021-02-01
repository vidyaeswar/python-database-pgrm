import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='userapplication',user='root',password='test1234')

if conn.is_connected():
	print("connected to mysql db")

cursor=conn.cursor()
try:

    cursor.execute("insert into application values(1,'vidya','vidya@gmail.com','hosur','91')")
    cursor.execute("insert into application values(2,'geetha','geetha@gmail.com','blr',89)")
    cursor.execute("insert into application values(3,'john','john@gmail.com','hyd',94)")
    cursor.execute("insert into application values(4,'soniya','soniya@gmail.com,'chennai',78)")
    conn.commit()
    print("record is added")
except:
	conn.rollback()

    

cursor.close()
  
conn.close()