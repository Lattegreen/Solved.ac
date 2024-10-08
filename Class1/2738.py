size = input()
k = size.split()
a = []
b = []
for n in range(0, int(k[0])):
	x = input()
	j = x.split()
	a.append(j)
	
for n in range(0, int(k[0])):
	y = input()
	j = y.split()
	b.append(j)

for n in range(0, int(k[0])):
	for m in range(0, int(k[1])):
		print(int(a[n][m]) + int(b[n][m]), end = "")
		print(" ", end="")
	print("")

