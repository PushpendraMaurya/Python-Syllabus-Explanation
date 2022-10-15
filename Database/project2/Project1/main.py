from dbhelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print("****Welcome to our Software**")
        print()
        print("Press 1 to insert  user")
        print("Press 2 to display the user")
        print("Press 3 to delete  user")
        print("Press 4 to update user")
        print("press 5 to exit the program")
        print()    
      
        try:
            choice=int(input("Enter Your Choice : "))
            if(choice ==1):
                #insert user
                uid = int(input("Enter Your Id :"))
                username =input("Enter Your User Name: ")
                userphone = input("ENter Your  Phone")
                
                db.insert_user(uid,username,userphone)
                
                
            elif choice ==2:
                #display user
                db.fetch_all()
                pass
            elif choice ==3:
                #delet user
                userid = int(input("Enter User Id :"))
                db.delete_user(userId)
                
            elif choice ==4:
                #update user
                uid = int(input("Enter  New Id :"))
                username =input("Enter  New User Name: ")
                userphone = input("ENter New  Phone")
                
                db.update_user(uid, newname, newphone)
                pass
            elif choice ==5:
                #exit
                break
            else:
                print("Invalid syntax so plz try again")
            
        except Exception as e:
            print(e)
            print("Invalid Details ! try Again...")
            

if __name__ == "__main__":
    main()

     
