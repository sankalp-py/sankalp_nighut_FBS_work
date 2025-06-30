# convert days into year , week , days 
days = int(input("Enter a days: "))
year = days // 365
days = days % 365
print(days)
week = days // 7 
days = days % 7
print(f'The year are {year} , week are {week} and days are {days}')