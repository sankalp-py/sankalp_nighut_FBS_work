#checking prime number in range 
num=int(input("Enter number:"))
for i in range(2,(num//2+1)):
    if(num%i==0):
        print(f"{num} is not prime number.")
        break
else:
    print(f"{num} is a primr number.")