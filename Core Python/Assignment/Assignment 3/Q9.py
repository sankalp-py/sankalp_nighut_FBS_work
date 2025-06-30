# showing grade based on 5 subject 
m1 = int(input("Enter a 1st subject marks: "))
m2 = int(input("Enter a 2sd subject marks: "))
m3 = int(input("Enter a 3rd subject marks: "))
m4 = int(input("Enter a 4th subject marks: "))
m5 = int(input("Enter a 5th subject marks: "))
total_marks = (m1 + m2 + m3 + m4 + m5) / 500 * 100
if (total_marks >= 80):
    print("First Class")
elif(total_marks >= 50):
    print("Second Class")
elif(total_marks >= 35):
    print("Pass")
else:
    print("Fail")