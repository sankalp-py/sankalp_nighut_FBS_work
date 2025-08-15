D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))
print("Minimum notes required:")

for note in D:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} : {count}")
