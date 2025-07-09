def sum_of_digits(n):

    if n == 0:
        return 0
    else:
       
        return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
if num < 0:
    num = abs(num)  
sum_digits = sum_of_digits(num)
print(f"Sum of digits of {num} is: {sum_digits}")