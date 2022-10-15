# # find the valid no in between start with 6,7,8,9 but have 10 digit in india 

# str = "7388006830","45875462","846587546","6598745698","3245876548"

# for i in str:
#     if i== i.len(10):
#         print("this is valid no " , i)
        
#     else:
#         print("Invaid matched ")
        


# import re
# x = "7388006830,45875462,846587546,6598745698,3245876548"
# a_string = x.split(",")
# matches = ["6,7,8,9"]
# match = re.findall(r'\d{10}', a_string)  
# ans = [i for i in match if any(map(i.startswith, matches))]
# print(ans)


st = "7388006830,45875462,846587546,6598745698,3245876548"
x = st.split(",")
ls = [i  for i in x if len(i) ==10]
als= []
for j in ls:
    if j[0] in ["9","8","7","6"]:
        als.append(j)
print(als)

