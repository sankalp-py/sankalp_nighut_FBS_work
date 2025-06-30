#checking number is divisible by given number and printing number
n = int(input("Enter a number you want to divede by:"))
s = int(input("Enter a number start divesion:"))
e = int(input("Enter a number end divesion:"))
for i in range (s,e+1):
    if i % n == 0:
        print(i)