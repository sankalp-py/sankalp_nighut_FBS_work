for i in range(1 ,5):
    print(" "*(5-i),end= "")
    for j in range (1, i+1):
        if j == 1 or j==i:
            print("1",end=" ")
        else:
            print(i - 1,end=" ")
    print()