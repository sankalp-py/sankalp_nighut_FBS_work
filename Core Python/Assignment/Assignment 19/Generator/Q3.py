def custom_range(start, stop=None, step=1):
    
    if stop is None:
        stop = start
        start = 0
    
    if step > 0:
        while start < stop:
            yield start
            start += step
    
    else:
        while start > stop:
            yield start
            start += step


for i in custom_range(1, 10 ):
    print(i, end = ' ')