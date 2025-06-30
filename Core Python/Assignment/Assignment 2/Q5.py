#counting selling price of item based on cost price and discount
cp = int(input("Enter a cost price: "))
dis = int(input("Enter a discount: "))
dp = cp * (dis / 100)
sp = cp - dp 
print("The selling price is: ", sp)