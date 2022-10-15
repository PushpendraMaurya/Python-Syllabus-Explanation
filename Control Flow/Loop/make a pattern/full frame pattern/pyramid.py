'''
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")

    for k in range(i):
        print("*",end=" ")

    for l in range(i + 1):
        print("*",end=" ")

    print()
    print()

'''
#second  opposite oyramid
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")

    for k in range(i):
        print("*",end=" ")

    for l in range(i + 1):
        print("*",end=" ")

    print()


for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")

    for k in range(2*i):
        print("*",end=" ")

    print()