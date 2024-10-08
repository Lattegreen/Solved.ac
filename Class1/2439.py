i = int(input())
for l in range(0, i):
    print(" " * (i - l - 1), end="", sep="")
    print("*" * (l + 1), end="", sep="")
    print("")
