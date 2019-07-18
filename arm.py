numb= int(input())
temp=numb
sum=0
while numb!=0:
    r=numb%10
    sum=sum+r**3
    numb=numb//10
if sum==temp:
    print("yes")
else:
    print("no")
