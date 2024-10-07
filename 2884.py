t = input()
l = t.split()
h = int(l[0])
m = int(l[1])
if m >= 45:
    print(h, m-45, sep=" ")
elif not h == 0:
    print(h-1, m+15, sep=" ")
elif h == 0:
    print(23, m+15, sep=" ")
