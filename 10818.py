n = int(input())
maxi = -1000000
mini = 1000000
k = input()
l = k.split()

for r in range(0, n):
    if int(l[r]) > maxi:
        maxi = int(l[r])
    if int(l[r]) < mini:
        mini = int(l[r])

print(mini, maxi, sep=" ")
