from collections import Counter
li=[60,60,50,50,40,30,2,0,22,22,1]
count = Counter(li)
new_li=[num for num in li if count[num]==1]
print(li)
print("remove  occurancey dupplication list:",new_li)
