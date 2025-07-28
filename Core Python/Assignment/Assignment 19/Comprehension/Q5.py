i = input("Enter a sentence: ")
w = [s for s in i.split() if len(s) < 5]
print(w)