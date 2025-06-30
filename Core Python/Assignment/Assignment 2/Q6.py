#calc the total salary based on da , ta ,hra
sa = int(input("Enter a salary: "))
da = sa *(10 / 100) 
print(da)
ta = sa *(12 / 100)
print(ta)
hra = sa *(15 / 100)
print(hra)
sa = sa + da + ta + hra
print("The total salary is: ", sa)