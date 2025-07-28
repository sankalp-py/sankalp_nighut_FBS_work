s = input("Enter a sentence :")
li =''.join([i for i in s if i.lower() not in 'aeiou'])
print(li)