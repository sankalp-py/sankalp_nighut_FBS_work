def leap(year):
    if ( year % 4 ==0):
        print(f'{year} is a leap year.')
    
    else:
        print(f'{year} is not a leap year.')
        
year = int(input("Enter a year: "))
leap(year)