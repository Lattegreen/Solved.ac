n = int(input())
EndNum = 1
LineNum = 1
if n == 1:
    print(1)
    exit(0)
while True:
    if EndNum >= n:
        print(LineNum-1)
        break
    EndNum = EndNum + ((LineNum-1) * 6)
    LineNum = LineNum + 1
