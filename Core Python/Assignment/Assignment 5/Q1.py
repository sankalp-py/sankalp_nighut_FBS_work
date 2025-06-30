#login checking 
us = 'yash'
passw ='yash1234'
for i in range(3):
    user = input("Enter user id:")
    password = input("Enter password:")
    if(us == user and passw == password):
        print("logged successfully.")
        break
    else:
        print("please try again...")
else:
    print("Invalid credentials....")