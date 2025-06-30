#checking percentage and average of an student 
st_no =int(input("Enter a number of student:"))
pects = []
for i in range(st_no):
    print(f'Enter marks for student{i + 1}:')
    total= 0
    for j in range(5):
        mark = float(input(f'Enter marks for Subject{j+1}:'))
        total+=mark
    pect = (total/500)*100
    pects.append(pect)
print("Percentages of all student:")
for i in range(st_no):
    print(f'student{i+1}:{pects[i]:.2f}%')
av =sum(pects)/st_no
print(f'Average percentage of the class:{av:.2f}%')
