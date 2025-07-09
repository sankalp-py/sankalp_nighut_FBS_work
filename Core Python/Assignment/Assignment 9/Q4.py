def sum_of_n(n):
    if n == 1:
        return 1
        return n + sum_of_n(n - 1)

num = int(input("Enter a number: "))
if num > 0:
    total = sum_of_n(num)
    print(f"Sum of first {num} numbers is: {total}")
else:
    print("Please enter a positive number.")