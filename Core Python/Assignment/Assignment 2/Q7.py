# sum of three digit number.
n = int(input("Enter a three digit no: "))
d1 = n % 10
n = n // 10
d2 = n % 10
d3 = n // 10
s = d1 + d2 + d3
print("The sum of three digit no: ", s)