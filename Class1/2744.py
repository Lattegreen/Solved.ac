char = input()
for letter in char:
    if letter.isupper():
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")