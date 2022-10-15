 # . character :- 
 
import re

s = "hello program this is python"

ptr = r"\.$"


x = re.findall(ptr,s)
print(x) 


