'''
Single inheritence is one of the fundamental concept in oops.

when  a  derived class inherit property only from a single base class is known as single inheritence


'''

#Example :- 


class parent:
    def data(self):
        self.name =name
        self.age = age


class child(parent):
    def info(self):
        print(self.name)
        print(self.age)

obj = child("pushpendra",22)
print(obj)