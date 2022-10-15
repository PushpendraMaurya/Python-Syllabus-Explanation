'''
Generator :- It is used to return a multiple of valaue as a one time 

it contains "yeild Keyword" 

generator used only one time data than erase the whole data  used only list

'''

#example :-  return keyword
'''def value():
    for i in range(1,11):
        return i

obj = value()
print(obj)'''

#example yield keyword
'''def value1():
    for i in range(1,11):
        yield i

x = value1()
print(list(x))
'''
# example make own yield keyword ..
x = [1,2,3,5,68,89]
for i in x:
    print(i, end=" ")
x = list(x)
print(x)