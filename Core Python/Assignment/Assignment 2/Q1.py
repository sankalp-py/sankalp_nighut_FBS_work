# convert hr min sec into sec 
h = int(input("Enter a hours: "))
m = int(input("Enter a minutes: "))
s = int(input("Enter a seconds: "))
s = (h * 3600) + (m * 60) + s
print("The total second is: ", s)