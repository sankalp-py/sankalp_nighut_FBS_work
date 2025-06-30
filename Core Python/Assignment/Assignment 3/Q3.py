# check triangle
a1 = int(input("Enter first angle of triangle: "))
a2 = int(input("Enter second angle of triangle: "))
a3 = int(input("Enter third angle of triangle: "))
if (a1 + a2 + a3) == 180:
    if(a1 >0):
        if(a2 > 0):
            if(a3 > 0):
                print("Triangle is valid.")
else:
    print("Triangle is not valid.")