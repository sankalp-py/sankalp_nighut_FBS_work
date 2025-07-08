n = int(input("Enter a dictionary:"))
dict = {}

for x in range(1, n+1):
    dict[x] = x * x 
    
print('Dictionary:', dict)