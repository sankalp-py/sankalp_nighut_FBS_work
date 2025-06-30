# WAP to calculat the percentage of 5 subjects 

s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
s4 = int(input("Enter marks of subject 4: "))
s5 = int(input("Enter marks of subject 5: "))
sum = s1 + s2 + s3 + s4 + s5
perc = (sum / 500) * 100
print("The percentage is: ", perc)
