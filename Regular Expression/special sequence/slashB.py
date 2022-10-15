'''
\B :- it is used to matched the  specific character  who are present but not at the beginning or end the word .




'''

import re
st = "this is python class"

x = re.findall(r"\Bpython", st)
print(x)