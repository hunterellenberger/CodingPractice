if __name__ == "__main__":
    pushes = int(input())
    days = list(map(int, input().split()))
    pushCount = 0
    pushDay = 0
    dirtiness = 0
    cleanups = 0

    for i in range(1, 366):
        dirtiness += pushCount

        if i == days[pushDay]:
            pushDay += 1
            if pushDay >= pushes:
                pushDay = -1
            pushCount += 1

        if dirtiness + pushCount >= 20:
            cleanups += 1
            pushCount = 0
            dirtiness = 0

    if pushCount > 0:
        cleanups += 1
    print(cleanups)
