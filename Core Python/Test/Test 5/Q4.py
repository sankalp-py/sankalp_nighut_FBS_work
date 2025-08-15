nums = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

print("Frequency Dictionary:", freq)
