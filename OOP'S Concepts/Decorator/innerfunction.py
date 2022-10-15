'''

define a function inside a function is known as inner function.

'''

#example :- 
'''def show(name):
    def msg():
        print("hwllo",name)

    return msg
s = show("pushpan")
s()


'''

#example :-  find a greatre no

def Parent(func):
    def child(a,b):
        return func(a,b)
    return child

@Parent
def finder(a,b):
    if a>b:
        return a,"is gretare"

    else:
        return b"is greatre"

x = finder(12,24)
print(x)
