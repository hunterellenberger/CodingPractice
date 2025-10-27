if __name__ == "__main__":
    x, y = map(int, input().split())
    possible = 0

    while x < y:
        divisible = 0
        if len(str(x)) == len(set(str(x))):
            for digit in list(str(x)):
                if int(digit) == 0:
                    divisible = 1
                    continue
                elif x % int(digit) > 0:
                    divisible = 1
            if divisible == 0:
                possible += 1
        x += 1

    print(possible)
