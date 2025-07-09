def count_digits(num):
    return len(str(num))
def armstrong_sum(num):
    n = count_digits(num)
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10
    return total
def is_armstrong(num):
    return num == armstrong_sum(num)
number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")