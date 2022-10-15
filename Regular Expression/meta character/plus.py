 # . character :- 
 
import re

s = "hello program this is python"

ptr = r"p.+h"


x = re.findall(ptr,s)
print(x) 


