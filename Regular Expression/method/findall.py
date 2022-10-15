'''
findall () :- findall basically work on find the arguments , and take two arguments
return on string data .  
its a unorderd collection return string .

1 - search pattern

2 - string data


'''

# example :- 
import re

st = "pushpendra is a good boy "

ptr = r"[c -m]"
x = re.findall(ptr,st)
print(x)