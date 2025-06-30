# calc the simple interest p , t ,r 
p = int(input("Enter the principal amount: "))
t = int(input("Enter the time in years: "))
r = int(input("Enter the rate of interest: "))
si = (p * t * r) / 100
print("The simple interest is: ", si)