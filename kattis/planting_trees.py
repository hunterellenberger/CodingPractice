if __name__ == "__main__":
    seeds = int(input())
    days = list(map(int, input().split()))
    days.sort(reverse=True)
    minDay = 0
    iter = 1

    for day in days:
        if day + iter >= minDay:
            minDay = day + iter
        iter += 1
    print(minDay + 1)
