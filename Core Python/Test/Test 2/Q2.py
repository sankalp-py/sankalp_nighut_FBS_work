n = int(input("Enter a 3 digit number: "))
first = n // 100
second = (n // 10) % 10
third = n % 10

if first == 2 * second and first == third // 2:
    print("Yes , you have done it")
else:
    print("Please try next time")
    