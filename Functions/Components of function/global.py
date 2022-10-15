'''
global keyword used to define a variable on outside  the function which is used to modifed or changable.
and i want acess  inside a function that time used global keyword and variable name inside a function .


'''

#example :- 
balance = 0
def deposite():
    global  balance #define variable to inside a function 
    print("Available balance is",balance)
    balance = balance+ 5000
    print("Available balance is ", balance)

deposite()