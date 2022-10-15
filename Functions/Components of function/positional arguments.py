'''

Postional arguments or keyword arguments :- 

Positional argument means that the argument must be provided in a correct position in a 
function call.


'''

#example :- 
def data (name = None, age = None):
    return "name is "+str(name) + " age is " +str(age)

obj = data(age=20,name="pushpendra")
print(obj)