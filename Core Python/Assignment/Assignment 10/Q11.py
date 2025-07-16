li=[1,2,3,0,0,0,33,66]
m=2
n=3
i=[]
for num in li:
    if num%m==0 and num%n==0:
        i.append(num)
        print(f"divisable by both :{m} and :{n} = {i}")