def odd():
    sum_odd = 0
    for i in range (1, n+1, 2):
        sum_odd += i
    print(f'Sum of all odd number is {sum_odd}')

n = int(input("Enter a number: "))
odd()