# checking triangle valid or not (sides)
s1 = int(input("Enter side 1:"))
s2 = int(input("Enter side 2:"))
s3 = int(input("Enter side 3:"))
if (s1 + s2 > s3):
    if(s1 + s3 > s2):
        if (s2 + s3 > s1):
            print("Triangle is valid.")
else:
    print("Triangle is not valid.")