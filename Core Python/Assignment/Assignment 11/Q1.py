li=[1,2,3,4,5,67,8,9]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"list:{li}\neven_list:{even}\nodd_list:{odd}")