#M
num1,num2=map(int,input().split())
sum=0
for n in range(num1,num2+1):
    if n == 2 or n == 3 or n == 5 or n == 7:
        sum=sum+1
    elif (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0) and (n != 1) and n > 0:
        sum=sum+1
print(sum)
