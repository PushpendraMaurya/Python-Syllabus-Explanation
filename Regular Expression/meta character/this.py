 # . character :- 
 
import re

s = "hello program this is python pushpendra pn" 

ptr = r"p\n"


x = re.findall(ptr,s)
print(x) 


