user = input("Enter a sentence: ")
l = {i : len(i) for i in user.split()}
print(l)