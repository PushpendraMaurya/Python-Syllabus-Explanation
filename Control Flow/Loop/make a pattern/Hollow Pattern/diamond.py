n = 5
for row in range(n):
    for col in range(n):
        if (row+col ==4 or col-row == 4 or row-col ==4 or row +col ==12):
            print("*",end=" ")

        else:
            print(" ",end= " ")

    print()