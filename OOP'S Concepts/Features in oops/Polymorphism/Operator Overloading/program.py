'''
Operator OverLoading :-
we have multiple of method i=with the same but different class is known as opeartor overloading.


'''

#example :- 
class A:
    def __init__(self,a):
        self.a = a

    def __add__(self,other):
        return self.a *other.a

class B:
    def __init__(self,a):
        self.a = a

    def __add__(self,other):
        return self.a / other.a

x = A(10)
y = B(20)
print(x+y)
print(x + y)