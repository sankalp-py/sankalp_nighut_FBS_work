n = int(input("Enter number of employees:"))

totalemps = 0

for i in range(1, n+1):
    basic = int(input("Enter a basic salary:"))
    
    if basic < 20000:
        da = basic *(10 / 100)
        ta = basic *(12 / 100)
        hra = basic*(15 / 100)
        
    else:
        da = basic * (15 / 100)
        ta = basic * (18 / 100)
        hra = basic * (20 / 100)
        
    salary = basic + da + ta + hra
    
    totalemps += salary

print(f'Total salary of employees:{totalemps}')