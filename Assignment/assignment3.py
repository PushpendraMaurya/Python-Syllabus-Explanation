
# list1 = [1,2,3]
# list2 = [1,2,3,4,5]

# def lister(a,b):
#     listed =[]
#     for i in list1:
#         for j in list2:
#             if i  not in list2:
#                 listed.append(i)

#             else:
#                 return list1
#     return list1

# obj = lister(list1,list2)
# print(obj)


#using comperhension :- 


#example :- 
'''def hell(a,b):
    char = []

    for i in a:
        for j in b:
            if i =="come":
                return "hello mr. come here"

            elif i =="go":

                return "mr. go"
            else:
                return "get lost chutiya"
    return char

obj = hell("come","go")
print(obj)
'''

'''list1 = [1,2,3]
list2 = [1,2,3,4,5]
def func(a,b):
    clean = []
    for i in a:
        for j in b:
            if i not in  b:
                return clean.append(i)

            

    return list1

obj = func(list1,list2)
print(obj)'''

# list1 = [1,2,3]
# list2 = [1,2,3,4,5]
# def func(a,b):
#     clean = []
#     for i in a:
#         for j in b:
#             if i !=j:
#                 return i

#             else:
#                 return clean.append(i)
        

# obj = func(list1,list2)
# print(obj)


'''list1 = [1,2,3]
list2 = [1,2,3,4,5]

for element in list1:
    if element in list2:
        list1.remove(element)
'''

from tkinter import Y


x = [1,2,3]
y = [1,3,4,5]

def func(a,b):
    for i in x:
        for j in y:
            if i in y:
                x.remove(i)

    return y 

obj = func(x,y)
print(obj)
                                                                                                                           