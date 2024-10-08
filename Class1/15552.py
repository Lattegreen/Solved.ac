import sys
loop = int(input())
for l in range(0, loop):
	x = sys.stdin.readline()
	y = x.split()
	a = int(y[0])
	b = int(y[1])
	print(a+b)
	
