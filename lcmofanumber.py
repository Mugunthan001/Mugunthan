import math
num1,num2=map(int,input().split())
res=math.gcd(num1,num2)
lcm=(num1*num2)/res
print(math.ceil(lcm))
