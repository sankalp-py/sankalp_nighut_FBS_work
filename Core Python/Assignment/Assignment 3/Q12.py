#checking the number is palindrome or not 
n = int (input("Enter a three digit number: "))
d1 = n % 10
n = n // 10 
d2 = n % 10 
d3 = n // 10
if d1 == d3:
    print("it's palindrome number. ")
else:
    print("not palindrome.")