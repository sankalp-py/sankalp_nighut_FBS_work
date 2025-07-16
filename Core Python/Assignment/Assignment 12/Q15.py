str1 = "apple"
str2 = "banana"

count1 = 0
for ch in str1:
    count1 += 1

count2 = 0
for ch in str2:
    count2 += 1

if count1 > count2:
    print("Larger string is:", str1)
elif count2 > count1:
    print("Larger string is:", str2)
else:
    print("Both strings are equal in length")
