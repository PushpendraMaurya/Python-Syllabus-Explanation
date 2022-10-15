'''class A:
    def test(self): #method
        self.a = 10
        self.b = 54
        return self.a +self.b

obj = A() #Instance
x = obj.test()
print(x)
print(obj.a)
print(obj.b)'''

#inherit the class



'''
contructor :- 
its a special method also call a intilize method. we dont need to call .this is automaticallu invoked when instace created.
this is first method of class.


Class:-  class is types of containr which is hold the programm untill return the data when will call the



 Self :- 
 
 self is supported variable.
 self is the refrence of object .
 this is used only inside  function
'''

'''
Object :- 
its a refrence of object.



'''


'''

There are two types of constructor 

1 with parameter
2 wthout parameter 
'''

#example :- 

#car details .
'''
class car :
    def thar(self):
        self.control = "automatic"
        self.roof = "yes"
    def tharinfo(self):
        print(self.control)
        print(self.roof)


    def bmw(self):
        self.control= "automatic"
        self.engine = "petrol"
    
    def bmwinfo(self):
        print(self.control)
        print(self.engine)

main = car()
main.bmw()
main.thar()
main.tharinfo()
main.bmwinfo()'''



class car :
    def thar(self):
        self.control = "automatic"
        self.roof = "yes"
    # def tharinfo(self):
    #     print(self.control)
    #     print(self.roof)


    def bmw(self):
        # self.control= "automatic"
        self.engine = "petrol"
    
    # def bmwinfo(self):
    #     print(self.control)
    #     print(self.engine)

class child(car):
    def info(self):
        
        print(self.control)


obj = child()
obj.info()

#example :- 




# def maxm(integar):
#     s = 0
#     for i in integar:
#         i >=s
#     return i

# obj = [2,3,4,5,6,78,9,9]

# x = maxm(obj)
# print(x)


# reverse a string

'''a = "pushpendra"

str = " "
for i in a:
    str = i + str

print("Reverse string is",str)
'''

# catch the int in the list

'''def catch(ls):
    for i in ls:
        return "myy no is"+ str(i)

intt = [1234567799765]

x = catch(intt)
print(x)'''


'''

Super Keyword :- 

super method is used to to access parent class property to be chiild class.
'''