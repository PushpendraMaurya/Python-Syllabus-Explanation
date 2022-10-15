'''
write a python program  and make a function takes two argument 
in list and return a difference both lost or  Unique Number. 

'''

'''list1 = [1,2,3,4,5,]
list2 = [1,2,3,4,5,6,7,8,9]

def function(a,b):
    for i in a:
        for j in b:
            if i is not b:
                return [i,j]

obj = function([list1],[list2])
print(obj)'''

'''list1 = [1,2,3,4,5,]
list2 = [1,2,3,4,5,6,7,8,9]
def function(a,b):
    unique = []
    for i in a:
        for j in b:
            if i is j:
                unique.append(i)
# obj = function([list1],[list2])
obj = function(list1,list2)
print(obj)'''


# def common(list1, list2):
#      data = []
#      for x in list1:
#          for y in list2:
#             if x not in list2:
#                 data.append(x)
#             else:
#                 return data

# obj = common([1,2,3,4,5], [5,6,7,8,9])
# print(obj)


# def common_data(list1, list2):
#      result = []
#      for x in list1:
#         for y in list2:
#              if x == list2:
#                  result.append(x)
#         return result
# print(common_data([1,2,3,4,5], [1,2,3,4,5,6,7]))


# def func(list1,list2):
#     compare = []
#     for i in list1:
#         for j in list2:
#             if (i in list2):
#                 compare.append(i)
#             else:
#                 return list2
#     # return compare

# obj = func([1,2,3],[1,2,3,4,5])
# print(obj)


# def unique(list1,list2):
  
#     # initialize a null list
#     unique_list = []
  
#     # traverse for all elements
#     for x in list1:
#         for y in list2:

#         # check if exists in unique_list or not
#             if x is not list2:
#                 unique_list.append(x)
#     return unique_list

#     # # print list
#     # for x in unique_list:
#     #     return x
  
  
# # driver code
# obj = unique([1,2,3],[1,2,3,4,5,6])
# print(obj)
  
'''
list1 = [1,2,3,4]
list2 = [1,2,3,4,5,6]
def lister(a,b):
    clean = []
    for i in range(list1,list2):
        if i in list2:
            clean.append(i)

    return clean


obj = lister(list1,list2)
print(obj)'''



# list_inp = [1,2,3,4,5] 

# res_list = []

# for item in list_inp: 
#     if item not in res_list: 
#         res_list.append(item) 

# print("Unique elements of the list using append():\n")    
# for item in res_list: 
#     print(item) 
      

list1 = [1,2,3]
list2 = [1,2,3,4,5]

def lister(a,b):
    listed =[]
    for i in list1:
        for j in list2:
            if i  not in list2:
                listed.append(i)
    return list1

obj = lister(list1,list2)
print(obj)
