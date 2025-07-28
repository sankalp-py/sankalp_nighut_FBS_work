def fibonacci_generator(l):
    a, b = 0, 1
    while a <= l:
        yield a
        a, b = b, a + b
        
l = int(input("Enter the Fibonacci limit: "))


print(f'Fibonacci sequence up to {l}:')
for n in fibonacci_generator(l):
    print(n, end=' ')
