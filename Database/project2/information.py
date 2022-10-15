import mysql.connector as connector # connector as aliaz

# con = connector.connect(host="localhost",port="3306",user="root",password="root",database="pythontest")

# print(con)

# creating a table 

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
        
        
        
        

#main coding

helper = DBHelper()
# helper.insert_user(102, "pushpendra", "7388006830") # call the insert
# helper.insert_user(103, "ritesh", "2345234") # call the insert
# helper.insert_user(104, "gaurab", "2341234") # call the insert
# helper.insert_user(105, "suraj", "12341324") # call the insert
# helper.insert_user(109, "mahon", "32345124") # call the insert
# helper.insert_user(1027, "kama", "29874524") # call the insert
# helper.fetch_all() # fetch data 
# helper.delete_user(102) # delete data 
# helper.delete_user(109) #deleet data 
# helper.fetch_all() #fetch data 
helper.update_user(102, 'Priyanshu', '8850660757') #update the info
# helper.fetch_all()


     
