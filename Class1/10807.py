n = int(input())
userinput = input()
userlist = userinput.split()
v = input()
counter = 0
for loop in range(0, n):
	if v == userlist[loop]:
		counter = counter + 1
print(counter)

