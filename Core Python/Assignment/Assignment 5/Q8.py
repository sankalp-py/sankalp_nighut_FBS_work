n=int(input("Enter the number:"))
fact = 1
sum = 0
for i in range(1,n+1):
    fact=fact*i
    sum+=fact
print("Factorial sum is :",sum)

exs= 0
for i in range(1,n+1):
    ex = n ** i
    exs += ex
print("Exponent sum :",exs)

geo_sum = 0
term = 1
for i in range(n):
    geo_sum += term
    term *= 2
print("Geomeric series sum: ",geo_sum)

series_sum = 0
for i in range(1, 11):
    term = (n ** i) / i
    series_sum += term

print("Sum of the series:", series_sum)

x = int(input("Enter value of x: "))
alt_sum = 0
sign = 1
power = 1
denominator = 1
for i in range(n):
    term = sign * (x ** power) / denominator
    alt_sum += term
    sign *= -1        
    power += 1
    denominator += 2 
print("Sum of the alternating series:", alt_sum)