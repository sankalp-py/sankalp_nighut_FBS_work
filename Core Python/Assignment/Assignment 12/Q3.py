str=input("enter the anagrams string:")
anagrams=str[::-1]
print(anagrams)
if(str==anagrams):
    print("it is anagrams string")
else:
    print("it is not anagrams string")