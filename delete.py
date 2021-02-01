import mysql. connector;
def delete(id):
    conn = mysql.connector.connect(host='localhost',database='employe',user='root',password='test1234')
    
    if conn.is_connected():
        print("connected to mysql")
        cursor=conn.cursor()
        str="delete for emp where id='%d'"
        args=(id)
        try:
            cursor.executed(str %args)
            conn.commit()
            print('employe deleted')
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
empId=int(input("enter emp Id:"))
delete(id)
        