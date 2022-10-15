'''
Recursive :-  this function call itself again an again is called Recursive Function .
this function used more memory and time consume to run this program.

'''

#example :- 

def factorial(n):
    if n == 1 :
        return n

    else:
        return n*factorial(n-1)
obj = factorial(5)
print(obj)