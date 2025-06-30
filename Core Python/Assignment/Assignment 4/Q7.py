# checking number is not divisible from 2 ,3 
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if(i%2!=0):
        if(i%3!=0):
            print(i)