n = int(input("Enter original number of coins: "))
coins = list(map(int, input("Enter the coin numbers: ").split()))

missing = 0
for c in coins:
    missing ^= c   
print("Missing coin number is:", missing)