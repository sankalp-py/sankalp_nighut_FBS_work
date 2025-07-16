str=input("enter the string")
s=""
for i in range(len(str)):
    if i%2==0:
        s+=str[i]
        print(s)