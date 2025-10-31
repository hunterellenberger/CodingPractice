if __name__ == "__main__":
    counted = []
    wrong = []
    total = int(input())
    for i in range(total):
        number = input()
        if number:
            counted.append(number)
        else:
            break

    counted = [int(i) for i in counted]
    if counted[0] != 1:
        for i in range(1, counted[0]):
            wrong.append(i)
    iter = 0
    while iter < total - 1:
        if counted[iter + 1] != counted[iter] + 1:
            for i in range(counted[iter] + 1, counted[iter + 1]):
                wrong.append(i)
        iter = iter + 1

    if not wrong:
        print("good job")
    else:
        for i in wrong:
            print(i)
