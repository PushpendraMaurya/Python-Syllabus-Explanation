'''

Method OverRiding :- In method overriding  have multiple of methods but different class 
each class perfom multiple of task  is known as method overriding .

'''
#example :- 
class parent:
    def car(self):
        print("Fortunar")


class child(parent):
    def car(self):
        print("Nexon")

obj = child()
obj.car()
