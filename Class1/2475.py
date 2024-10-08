s = input()
l = s.split()
k = 0
for x in range(0, 5):
    k = k + (int(l[x]) * int(l[x]))
print(str(k)[-1])
