#user login using random number pin to login 
import random
user = input("Enter a user id: ")
pwd = input("Enter a pass:")
if user == 'admin':
    if pwd == '1234':
        cap = random.randint(1000,9999)
        print("captcha: ", cap)
        us_in = int(input("Enter a captch:"))
        if us_in == cap:
            print("login succesfully.")
        else:
            print("invalid captcha.")
else:
    print("invalid userid.")