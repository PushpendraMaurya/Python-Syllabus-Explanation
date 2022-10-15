import mysql.connector as connector # connector as aliaz

class DBHelper:
    def __init__(self):
        self.con= connector.connect(host="localhost",port="3306",user="root",password="root",database="pythontest")
        
        query = "create table if not exists user (userId int primary key,userName varchar(200), phone varchar(10))"
        cur= self.con.cursor()
        cur.execute(query)
        # print("created ")
        
# insert the table
    def insert_user(self,userid,username,phone):
        query ="insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        # print(query)
        cur = self.con.cursor() # fire the query 
        cur.execute(query)  #ecute 
        self.con.commit() # commit for save the data 
        print("User Saved To db")
        
# fetch the all data 
    def fetch_all(self):
        query = "select * from user "
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            # print(row)
            print("UserID :",row[0])
            print("UserName :",row[1])
            print("User Phone ",row[2])
            print()
            print()
 
# deleete the user info           
    def delete_user(self,userId):
        query = "delete from user where userId={}".format(userId)
        # print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Deleted")
        
    def update_user(self,userId,newName,newPhone):
        query = "update  user set userName ='{}',phone='{}' where userId={}".format(newName,newPhone,userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Info Is Updated")
        
        
        
        
