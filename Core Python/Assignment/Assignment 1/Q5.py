# calc the compound interest p , t ,r
p = int(input("Enter the principal amount: "))
t = int(input("Enter the time in years: "))
r = int(input("Enter the rate of interest: "))
ci = p * ((1 + (r / 100)) ** t) - p
print("The compound interest is: ", ci)