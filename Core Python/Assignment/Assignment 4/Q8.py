#checking number is divisiable by 5 ,7
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if(i%7==0):
        if(i%5==0):
            print(i)