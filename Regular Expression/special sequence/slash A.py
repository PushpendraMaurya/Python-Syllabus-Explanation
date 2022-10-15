'''
\A :- its return if character  is matched at the  begginning  of the string .


'''
import re
st = "python class squad"

x = re.findall("\Apython",st)  #true
x1= re.findall("\Aclass", st)  #error
print(x)
print(x1) 