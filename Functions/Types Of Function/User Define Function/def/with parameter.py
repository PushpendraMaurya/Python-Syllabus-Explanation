
'''
its a call by value 
'''

#example :- 

# find a factorial using call by value  or function with parameter.




def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact*i

    print("factiral of " + str(n) + " = " + str(fact))


a = 5
factorial(a)
factorial(8)
