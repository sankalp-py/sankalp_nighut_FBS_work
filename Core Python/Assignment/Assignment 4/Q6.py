#checking prime number or not 
n=int(input("Enter the number:"))
for i in range(2,(n//2)+1):
    if(n%2==0):
        print("it is not prime no...")
    else:
        print("it is prime no...")
    break
        