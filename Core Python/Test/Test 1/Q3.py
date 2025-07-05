km = float(input("Enter a distance:"))
cm = km * 100000
m = cm // 100
cm = cm % 100
print(f'The meters are {m} or a centimeter are{cm}.')