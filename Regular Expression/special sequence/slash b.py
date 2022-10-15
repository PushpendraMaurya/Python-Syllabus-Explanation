'''slash b  :- bascically find or match the character at the begining or ending in the word .



'''

import re

st = "python is the top of class "
st1 =" is the   squad python class"

x = re.findall(r"\bpython", st)

x1 = re.findall(r"python\b", st1)
print(x1)

print(x)