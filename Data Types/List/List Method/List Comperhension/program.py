'''

List Comperhension :- its a very easy and compact syntax to write the code
 and wirte code to  inside the [] square bracket only .

this is work only mutable data .

'''

# basic example :- Find the cube .
'''
ls = [1,2,3,4,5]
cube = []
for i in ls:
    cube.append(i**3)

print(cube)
'''

# using comperhension :-
'''
ls = [1,2,3,4,5]
cube = [i**3 for i in ls]
print(cube)

'''

# find odd and even :-

ls =[1,2,3,4,5]

cube = [ i if i%2 ==0 else "odd"   for i in ls]
print(cube)