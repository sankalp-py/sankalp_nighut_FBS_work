def m(f):
    dic = {}
    
    def wrapper(*args):
        if args in dic:
            return dic[args]
        result = f(*args)
        dic[args] = result
        return result
    return wrapper

@m
def fibo(n):
    if n <= 1:
        return n 
    return fibo(n - 1) + fibo(n - 2)

print(fibo(10))