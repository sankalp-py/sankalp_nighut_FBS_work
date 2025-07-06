def sum():
    n = int(input("Enter a number:"))
    sum = 0
    for i in range(1,n+1):
        sum += i 
    print(f'The sum of {n} is {sum}')
    fact = 1
    f_sum = 0
    for i in range(1, n+1):
        fact = fact*i
        f_sum += fact 
    print(f'The factorial sum of {n} is {f_sum}')
    exs= 0
    for i in range(1,n+1):
        ex = n ** i
        exs += ex
    print("Exponent sum :",exs)
sum()