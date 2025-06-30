k = 7
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    
    for j in range(1, k+1):
        print(' ', end=' ')
    k=k-2
    
    for j in range(i, 0, -1):
        if i == 5:
            if j - 1 != 0:
                print(j - 1, end=' ')
        else:
            print(j, end= ' ')
    print()