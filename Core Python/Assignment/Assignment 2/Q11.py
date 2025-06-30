# calc the minimum number of notes
amt = int(input("Enter a amount: "))
n2000 = amt // 2000
amt = amt % 2000
n500 = amt // 500
amt = amt % 500 
n200 = amt // 200
amt = amt % 200
n100 = amt // 100
amt = amt % 100
n50 = amt // 50 
amt = amt % 50
n20 = amt // 20 
amt = amt % 20
n10 = amt // 10 
s = n2000 + n500 + n200 + n100 + n50 + n20 + n10  
print(f'2000 = {n2000} , 500 = {n500} , 200 = {n200} , 100 = {n100} , 50 = {n50} , 20 = {n20} , 10 = {n10}.')
print("The total number of notes is: ", s) 