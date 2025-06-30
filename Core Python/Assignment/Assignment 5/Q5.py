#minimum notes number using looping 
amount = int(input("Enter the amount:"))

notes = [2000, 500, 200, 100, 50, 20, 10,]

print("Minimum number of notes:")

for i in notes:
    if amount >= i:
        count = amount // i
        print(f"{i} x {count} = {i * count}")
        amount = amount % i
