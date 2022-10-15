n = 5
for row in range(n):
    for col in range(n):
        if(row ==4 or row+col == 4 or col-row ==4 or col ==4):
            print("*",end=" ")

        else:
            print(" ",end= " ")

    print()
