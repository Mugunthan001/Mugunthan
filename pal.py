numb = int(input())
temp = numb
reve = 0
while temp != 0:
	reve = (reve * 10) + (temp % 10)
	temp = temp // 10
if numb == reve:
	print("yes")
else:
	print("no")
