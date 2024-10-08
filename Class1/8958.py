rep = int(input())
for _ in range(0, rep):
    TestResult = input()
    streak = 1
    point = 0
    for problem in TestResult:
        if problem == 'O':
            point = point + streak
            streak = streak + 1
        elif problem == 'X':
            streak = 1
    print(point)
