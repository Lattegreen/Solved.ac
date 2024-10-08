l = []
l2 = []
for k in range(0, 10):
    l.append(int(input()) % 42)
    l2.append(l[k])
result = 0
for x in l:
    if l2.count(x) == 1:
        result += 1
    else:
        l2.remove(x)
print(result)