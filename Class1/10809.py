chars = "abcdefghijklmnopqrstuvwxyz"
UserString = input()
for letter in chars:
    if letter not in UserString:
        print(-1, end=" ")
    else:
        print(UserString.index(letter), end=" ")
