import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="test1234",database="student")
if mydb.is_connected():
    print("connected to database")
    cursor=mydb.cursor()
    mycursor=mydb.cursor()
sql = "INSERT INTO student (name,course,address,phone) VALUES (%s, %s)"
val = ('vidya','bca'',hosur','1234')
sql="INSERT INTO student(name,course,address,phone) VALUES (%s,%s)"
val=('geetha','betech','banglore','123456789') 
sql="INSERT INTO student(name,course,address,phone) VALUES (%s,%s)"
val=('kranthi','betech','banglore','8904831531') 

mydb.commit()

print(mycursor.rowcount, "record inserted.")