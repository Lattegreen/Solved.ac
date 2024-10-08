participants = int(input())
shirts = input()
ShirtsList = shirts.split()
bundle = input()
BundleSize = bundle.split()
PenBundle = participants // int(BundleSize[1])
PenSingle = participants - PenBundle * int(BundleSize[1])
ShirtBundle = 0
for ShirtSize in ShirtsList:
    if int(ShirtSize) % int(BundleSize[0]) == 0:
        ShirtBundle = ShirtBundle + (int(ShirtSize) // int(BundleSize[0]))
    else:
        ShirtBundle = ShirtBundle + (int(ShirtSize) // int(BundleSize[0])) + 1
print(ShirtBundle)
print(PenBundle, PenSingle)
