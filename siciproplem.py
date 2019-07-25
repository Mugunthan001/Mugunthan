import math
amt,time,rate=map(int,input().split())
final=(amt*time*rate)/100
fi=math.floor(final)
print(fi)
