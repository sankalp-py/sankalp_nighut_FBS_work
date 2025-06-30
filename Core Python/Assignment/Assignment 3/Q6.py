# check the profit and loss
cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))
if (sp > cp):
    print("Profit is", sp - cp)
elif (sp < cp):
    print("Loss is", cp - sp)
else:
    print("No profit no loss.")