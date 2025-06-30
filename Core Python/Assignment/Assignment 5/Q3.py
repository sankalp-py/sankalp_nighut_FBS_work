#calc the discount based on age in (looping)
pas_no =int(input("Enter a number of pasenger:"))
ticket=int(input("Enter a ticket amount:"))
total_amt=0
for i in range(1,pas_no+1):
    age=int(input(f'Enter the pasenger age{i}:'))
    if(age <12):
        dic=ticket*0.3
        
    elif(age >59):
        dic=ticket*0.5
        
    else:
        dic=0
        
    amt=ticket-dic
    total_amt=amt+total_amt
print("Total amount:",total_amt)        
            
        
