s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
i = s1.intersection(s2)
s1.difference_update(i)
print(s1)