def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

def is_armstrong(num):
    original = num
    digits = count_digits(num)
    sum_of_powers = 0
    
    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** digits
        num = num // 10

    return original == sum_of_powers

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
