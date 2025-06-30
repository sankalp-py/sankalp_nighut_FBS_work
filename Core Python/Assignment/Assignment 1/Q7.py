#Finding Roots of quadratic equation 
a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
c = int(input("Enter a value: "))
d = b**2 - 4 * a * c 
print(d)
x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)
print(f'The root is {x1} and {x2}')