#checking armstorng number 
s = int(input("Enter a start of range:"))
e = int(input("Enter a ead of range:"))
for i in range(s, e +1):
    d = len(str(i))
    sum = 0
    t = i
    while t > 0:
        dt = t % 10
        sum += dt ** d
        t//=10
    if sum == i:
        print(i)