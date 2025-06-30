#cheching vowel and constant
ch = input("Enter a alphabet: ")
if ch in 'aeiou':
    print('vowel')
elif ch in 'bcdfghjklmnpqrstvwxyz':
    print('constant')
else:
    print('not alphabet')