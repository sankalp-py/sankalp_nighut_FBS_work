# checking triangle is equilateral, isosceles or scalene
s1 = int(input("Enter side 1:"))
s2 = int(input("Enter side 2:"))    
s3 = int(input("Enter side 3:"))
if (s1 == s2):
    if (s2 == s3):
        print("Triangle is equilateral.")
elif(s2 == s3):
    print("Triangle is isosceles.")
elif(s1 == s3):
    print("Triangle is isosceles.")
else:
    print("Triangle is scalene.")