for i in range (1, 6):
    for j in range (1, 6-i):
        print(' ', end =' ')
    for j in range (1):
        print("*", end=' ')
    for j in range(4):
        print(' '*i, end=' ')
    for j in range(1):
        print("*",end=' ')
    print()
print()