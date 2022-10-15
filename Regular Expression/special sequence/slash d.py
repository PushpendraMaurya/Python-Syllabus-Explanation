'''
\d :- it is use to find where the number is present 

'''
import  re
st = "python 876587696 class 86586"

s = re.findall(r"\d",st)
print(s)