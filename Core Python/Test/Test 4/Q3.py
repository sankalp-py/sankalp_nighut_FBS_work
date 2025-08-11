rows = 12   
cols = 22   

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1:  
            print("*", end="")
        elif j == cols - i - 1:      
            print("*", end="")
        else:
            print(" ", end="")
    print()
