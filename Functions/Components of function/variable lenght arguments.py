'''
variable lenght arguments used to add the unlimited of data in a function where i dont how many have arguments that time used and sent the data to the function caller

used a *args as a paramter

'''

#example :- 
def sum1(*data):
    unlim = data
    s = 0
    for i in data:
        s = s+i
    return s

obj = sum1(23,23)
print(obj) 

