# checking number is strong number or not 
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
temp = num
sum_of_factorials = 0

while temp > 0:
    digit = temp % 10
    sum_of_factorials += factorial(digit)
    temp //= 10

# Check if it's a Strong Number
if sum_of_factorials == num:
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")
