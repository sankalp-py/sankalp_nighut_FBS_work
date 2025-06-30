#calc the discount based on age 
t_amt = int(input("Enter a amount: "))
p1 = int(input("Enter your age: "))
p2 = int(input("Enter your age: "))
p3 = int(input("Enter your age: "))
p4 = int(input("Enter your age: "))
p5 = int(input("Enter your age: "))
if (p1 <= 12):
    t_p1 = (t_amt * 30/100)
    t_p1 = t_amt - t_p1
    print(t_p1)
elif(p1 >= 59):
    t_p1 =(t_amt * 50/100) 
    t_p1= t_amt - t_p1
    print(t_p1)
else:
    t_p1 = t_amt
if (p2 <= 12):
    t_p2 = (t_amt * 30/100)
    t_p2 = t_amt - t_p2
    print(t_p2)
elif(p2 >= 59):
    t_p2 =(t_amt * 50/100)
    t_p2= t_amt - t_p2
    print(t_p2)
else:
    t_p2 = t_amt
if (p3 <= 12):
    t_p3 = (t_amt * 30/100)
    t_p3 = t_amt - t_p3
    print(t_p3)
elif(p3>= 59):
    t_p3 =(t_amt * 50/100)
    t_p3= t_amt - t_p3
    print(t_p3)
else:
    t_p3 = t_amt
if (p4 <= 12):
    t_p4 = (t_amt * 30/100)
    t_p4 = t_amt - t_p4
    print(t_p4)
elif(p4 >= 59):
    t_p4 =(t_amt * 50/100)
    t_p4= t_amt - t_p4
    print(t_p4)
else:
    t_p4 = t_amt
if (p5 <= 12):
    t_p5 = (t_amt * 30/100)
    t_p5 = t_amt - t_p5
    print(t_p5)
elif(p5 >= 59):
    t_p5 =(t_amt * 50/100)
    t_p5= t_amt - t_p5
    print(t_p5)
else:
    t_p5 = t_amt
t_p = t_p1 + t_p2 + t_p3 + t_p4 + t_p5
print(t_p)