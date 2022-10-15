'''
there is no any way to direct access .


but can also access data in indirect way  and return in string format .

'''
# Using First Way :- 
'''
s = {"python","html","css","sql"}

c = " "

for i in s:
    if i == "python":
        c = i 
print(c)

'''

# using second way :- 
'''
s = {"python","html","css","sql"}
for i in s:
    print(i)
    
   ''' 
   
   
# usinf third way typecasting :- 

s = {"python","html","css","sql"}
s = list(s)
print(s)