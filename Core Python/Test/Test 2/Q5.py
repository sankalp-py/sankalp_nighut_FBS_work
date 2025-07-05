p1 = int(input("Enter a 1 price:"))
p2 = int(input("Enter a 2 price:"))
p3 = int(input("Enter a 3 price:"))
p4 = int(input("Enter a 4 price:"))
p5 = int(input("Enter a 5 price:"))

total_a = p1 + p2 + p3 + p4 + p5
gst = total_a * 18 /100
amount = total_a + gst
print("Total bill is :", amount)