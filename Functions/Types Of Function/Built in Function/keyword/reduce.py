'''
 reduce :-  it  is used to reduced the data into single data.
 its not supported  python then i will import "functools" 



'''
import functools


ls = [1,2,45,6,7,89,90,3]
def test(a,b):
    return (a+b)

x = functools.reduce(test,ls)
print(x)
