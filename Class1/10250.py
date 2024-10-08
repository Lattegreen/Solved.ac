t = int(input())
for _ in range(0, t):
    line = input()
    l = line.split()
    h = int(l[0])
    w = int(l[1])
    n = int(l[2])
    x = 1
    while True:
        if n <= h:
            if x >= 10:
                print(n, x, sep="")
            else:
                print(n, 0, x, sep="")
            break
        else:
            n = n-h
            x = x + 1
