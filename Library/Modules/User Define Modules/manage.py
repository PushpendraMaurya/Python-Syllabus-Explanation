#first we can use files that time import library is known as inside flies folder library .
from files import addition,factorial,multiplication,pattern,subtraction

#check the directry of files folder 

# print(dir(files)) :- check the directry

# whiile True:
# addition modules files access
# b = int(input("Enter Your Second : "))
# a = int(input("Enter Your First : "))

# help(files) :- help the files

add = addition.addition(12, 23)
print(f"This is addition for two no :{add}\n")


# subtraction modules files access 
# a = int(input("Enter Your First : "))
# b = int(input("Enter Your Second : "))

sub = subtraction.substraction(10, 20)
print(f"This is Subtraction is {sub}\n")

# this is multiplication

mul = multiplication.multiplication(10, 5)
print(f"This is multiplication {mul}\n")

#this is pattern design 

pattern.pattern(5)




