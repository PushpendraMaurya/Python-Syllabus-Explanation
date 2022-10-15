'''
Method OverLoading does not support in python than i need import theri module name is "multipledispatch"

In method overloading have multiple object with same name but different parameter is known as method overloading

method overloading used decorator in their code.
'''

# bsic Example :- 
from multipledispatch import dispatch

class Map:
    @dispatch()
    def add(self):
        return 10+20
    @dispatch(int)
    def add(self,a):
        return a+20
    @dispatch(int,int)
    def add(self,a,b):
        return a+b

obj= Map()
a = obj.add()
a1 = obj.add(12)
a2 = obj.add(12,45)
print(a)
print(a1)
print(a2)

