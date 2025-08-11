def print_factors(num):
    print(f"Factors of {num}:", end=" ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()

n = int(input("Enter a number: "))
print_factors(n)
