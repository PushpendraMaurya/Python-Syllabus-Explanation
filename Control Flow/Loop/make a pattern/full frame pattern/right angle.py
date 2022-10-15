'''n = 5
for i in range(0,n,+1):
    for j in  range(0,i,+1):
        print("*",end=" ")

    print()'''

#second method

'''n = 9
for i in range(n):
    for j in range(i-1):
        print("*",end=" ")

    print()'''


n = 5
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")

    print()