for i in range (1, 6):
    print(' '*(5-i),end = '')
    for j in range (1, i+1):
        if i == 5 or j == 1 or j == i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()