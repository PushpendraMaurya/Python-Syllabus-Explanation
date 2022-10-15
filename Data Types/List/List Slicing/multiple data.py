'''

multiple data as known as slicing.

where i can use to give a position as well as steps where is give a element between having rANGE .

'''

'''

i have a 10 elemtns 1 to 10 if i want access data  between 3 to 6. that time i will use slicing to access the data.

noted :- list slicing to find the elemnt start with 1 not 0 .

ls = [1,2,3,4,5,6,7,8]

s = ls[2,5]

print(s)
'''
# positive value  count between left to right .

ls = [1,2,3,4,5,6,7,8]

s = ls[2:5]

print(s)


# negativ value count between right to left .

# ls = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
ls = [1,2,3,4,5,6,7,8]

s = ls[-1:-5 :-1]
print(s)