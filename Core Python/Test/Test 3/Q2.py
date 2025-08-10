n = int(input("Enter the value of n:"))

sumn = 0

for i in range(1, n +1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sumn += i/ fact
print("Sum of series:", sumn)