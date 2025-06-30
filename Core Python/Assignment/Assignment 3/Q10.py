# eligible or not for marry 
g = input("Enter your gender (m/f):")
age = int(input("Enter your age: "))
if g == "m":
    if(age >= 21):
        print("eligible")
    else:
        print("uneligible")
elif g == "f":
    if(age >= 18):
        print("eligible")
    else:
        print("uneligible")
else:
    print("invalid gender.")