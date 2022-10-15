import main as m
print("\n*****************************Welcome To  My Calculator__*********************************\n")
print()
while True:
    
    print("1 - Additions\n2 - Substraction\n3 - Multiplications\n4 - Divisions\n5 - Factorials\n6 - Percentages\n7 - For Exit")
    print()
    ch = input("Enter Your Choice: ")
    if ch == "1":
        a = int(input("Enter Your Additions :"))
        b = int(input("Enter Your Additions :"))
        add = m.addition(a, b)
        print("This is addition",add)
        
    elif ch == "2":
        a = int(input("Enter Your Subtraction :"))
        b = int(input("Enter Your Subtraction :"))
        sub = m.substraction(a, b)
        print("This is Subtractions",sub)
    elif ch == "3":
        a = int(input("Enter Your Multiplication :"))
        b = int(input("Enter Your Multiplication :"))
        mul = m.multiplication(a, b)
        print("This is MUltipliations",mul)
    
    elif ch =="4":
        a = int(input("Enter Your Division :"))
        b = int(input("ENter your Division :"))
        div =m.division(a, b)
        print("This is Division ",div)
            
    elif ch =="5" :
        obtain = int(input("Enter Your obtain :"))
        total = int(input("ENter Your Total"))
        per = obtain/total*100
        print("This is Yout percentages",per)
        
   
    elif ch =="6":
        n = int(input("Enter Your Factorial NO :"))
        fact = m.factorial(n)       
        print("\nfacotorial is ",fact) 
    elif ch =="7":
        print("\nExit  Application !,Thanks for you coming ,")
        break
        
    else:
        print("\n Invalid No , Try Again...!")
    