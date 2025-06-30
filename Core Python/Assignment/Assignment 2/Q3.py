#Feet and inches convert into meter and centimeter
f = int(input("Enter a feet: "))
i = int(input("Enter a inche: "))
i = (f * 12) + i
cm = i * 2.54
m = cm // 100
cm = cm % 100
print(f'The meter is {m} and centimeter is {cm}.')