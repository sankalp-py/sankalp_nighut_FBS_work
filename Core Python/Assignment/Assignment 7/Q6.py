for i in range (1, 6):
    k=0
    for j in range(i-7,-1):
        a=i+k
        if i == 2 and (a == 3 or a == 4)or(i == 3 and a == 4):
            print(' ',end=' ')
        else:
             print(a,end=' ')
        k+=1
    print()