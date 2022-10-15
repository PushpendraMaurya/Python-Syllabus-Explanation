'''
format Method ():- formate method it is use in string to without the break
 as well as pass the whole data into a single string  .


'''

age = 22
name = "pushpendra"

result = "Name is "+str(name) +" and "+" Age is " +str(age)   #Normal Method


result1 = "Name is {} and Age is {}".format(name,age)  #Using Without argument positions


result2 = "Name is {0} and age is {1}".format(name,age) # using with positions arguments

result3 = "Name is {1} and age is {0}".format(age,name) # without arraged

print(result)
print(result1)
print(result2)
print(result3)