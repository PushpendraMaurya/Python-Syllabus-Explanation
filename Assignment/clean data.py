'''ls =["a","#","%","&","!","4","6","9"]

def cleandata(data):
    clean=[]
    for i in ls:
        if i.isdigit():
            clean.append(i)
        
    return clean

x = cleandata(ls)
print(x)'''

'''
str = "123!@#$"  
if str.isdigit() == True:  
    print("String is digit")  
else:  
    print("String is not digit") 
    
'''




# ls = ['1','3','/','5','7','*']
# clean = []
# def func(data):
#     global clean
#     for i in ls:
#         if i.isdigit:
#             clean.append(i)
#     return clean

# obj = func(ls)
# print(obj)

#how to filterd data using own code .

ls = ["1","@","#","$","2","4","6","*"]

def cleandata(data):
    clean = []
    for i in ls:
        if i.isdigit():
            clean.append(i)
    return clean

obj = cleandata(ls)
print(obj)