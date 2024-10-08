n = int(input())
userinput = input()
CharList = userinput.split()
prime = 0
for number in CharList:
    temp = 2
    while True:
        if int(number) == 1:
            break
        if temp >= int(number):
            prime = prime + 1
            break
        if int(number) % temp == 0:
            break
        temp = temp + 1
print(prime)