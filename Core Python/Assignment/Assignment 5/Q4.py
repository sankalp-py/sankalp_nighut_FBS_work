#checking armstrong number using looping 
num=int(input("Enter a number:"))
tem = num
num1 = num
count = 0
sum = 0
while(tem>0):
    d = tem % 10
    tem = tem // 10 
    count+=1
for i in range(count):
    d = num % 10
    sum1 = d ** count
    sum += sum1
    num = num // 10
if sum == num1:
    print(f'{num1} is an armstrong number.')
else:
    print("not")