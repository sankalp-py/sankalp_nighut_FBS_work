def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse

num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("Reversed number is:", reversed_num)
