BreakDown = int(input())
mini = BreakDown - (9 * len(str(BreakDown)))
if mini < 0:
    mini = 1
result = False
for candidate in range(mini, BreakDown):
    temp = 0
    for numbers in str(candidate):
        temp = temp + int(numbers)
    CandidateBreakdown = candidate + temp
    if CandidateBreakdown == BreakDown:
        print(candidate)
        result = True
        break
if not result:
    print(0)