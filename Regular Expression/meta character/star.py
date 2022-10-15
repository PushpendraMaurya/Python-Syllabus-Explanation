 # . character :- 
 
import re

s = "hello program this is python"

ptr = r"o.*python"


x = re.findall(ptr,s)
print(x) 


