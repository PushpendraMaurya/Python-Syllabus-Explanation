# Continue :-

'''
It is used to end the current iterator in the given list and continue the next iteration
work only inside a loop work us range bases
'''
#Example : -

# for i in range(5):
#     if i == 4:
#         continue
#     print(i)
        

# loop from 1 to 10
for i in range(1, 11):
 
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")