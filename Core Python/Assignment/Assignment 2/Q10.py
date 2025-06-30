# reversing the three digit number
n = int (input("Enter a three digit number: "))
d1 = n % 10
n = n // 10 
d2 = n % 10 
d3 = n // 10
rn = (d1 * 100) + (d2 * 10) + d3 
print("The reversed number is: ", rn)