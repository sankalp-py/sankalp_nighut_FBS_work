def print_fibonacci(terms):
    a, b = 1, 1
    print(a, end=' ')
    if terms > 1:
        print(b, end=' ')
    for _ in range(3, terms + 1):
        c = a + b
        print(c, end=' ')
        a, b = b, c

terms = int(input("Enter the number of terms: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    print_fibonacci(terms)
