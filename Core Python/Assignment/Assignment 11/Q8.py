num = 100

for row in range(10):
    line = []
    for _ in range(10):
        line.append(num)
        num -= 1

    if row % 2 != 0: 
        line.reverse()

    for n in line:
        print(f"{n:3}", end=" ")
    print()
