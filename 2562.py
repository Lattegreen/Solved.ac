largest = 0
num = 0
for l in range(0, 9):
    x = int(input())
    if x > largest:
        largest = x
        num = l
print(largest)
print(num + 1)