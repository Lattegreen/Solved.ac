a = input()
a1 = a.split()
n = int(a1[0])
x = int(a1[1])
userinput = input()
userlist = userinput.split()
for l in range(0, n):
	if (int(userlist[l]) < x):
		print(userlist[l], end=" ")

