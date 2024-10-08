while True:
    UserInput = input()
    if UserInput == "0 0 0":
        break
    else:
        lengths = UserInput.split()
        a = int(lengths[0])
        b = int(lengths[1])
        c = int(lengths[2])
        if (a * a + b * b) == (c * c):
            print("right")
        elif (b * b + c * c) == (a * a):
            print("right")
        elif (c * c + a * a) == (b * b):
            print("right")
        else:
            print("wrong")
