'''
decorator :- it a tool in python . to provide a give abitlity to change the behavior of class or method . 

There are two types decorator .

1 - Built in Decorator

        there are 3 types :- 
                 static - @staticmethod
                 class - @classmethod

2 - User Define Decorator


        user define decroator used inner function to write the own code

        inner function :- inner function define a function than define inside the function is known as inner function


'''

'''
In python decorator pass the function as a arguments.

'''
def add(a,b):
    return (a+b)

def per(func,a,b,total = 100):
    obt = func(a,b)
    return obt/total*100

obj = add
p =per(obj,25,43)
print(p)