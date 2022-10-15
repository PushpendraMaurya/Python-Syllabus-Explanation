 # Filter :-  Filter function it used to get filtered the element into the  list . its takes two arguments first is 
 # function name and second is iterable name its works only the list .

 #example :-



'''ls = [1,2,3,4,56,65]
def func(ls):
    if ls%2!=0:
        return ls

x = filter(func,ls)
print(list(x))

'''
#example usinf lambda
'''ls = [1,2,3,4,56,65]
x = filter(lambda ls :ls if ls%2!=0 else None)
print(x)
'''
 
 #example 3 :- filterd the sum of value .

x = [-1,-2,-3,-4,1,2,3,-6,-4,-4,54,-65,-3]
def func(x):
    if x >0:
        return x

p = filter(func,x)
print(list(p))
