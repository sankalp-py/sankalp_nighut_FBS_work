li=[60,50,40,30,30,2]
user_element=int(input("enter the element:"))
if user_element in li:
    count=li.count(user_element)
    print(f"{user_element} it is a {count} time repeated into list")
else:
    print(f"{user_element} it is a not repated number")