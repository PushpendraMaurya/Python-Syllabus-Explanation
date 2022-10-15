 # . character :- 
 
import re

s = "hello program this is pooon"

ptr = r"p.{3}n"


x = re.findall(ptr,s)
print(x) 


