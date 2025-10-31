if __name__ == "__main__":
    moves = int(input())
    string = input()

    if string[0] == "R":
        curr = 1
    else:
        iter = 0
        while string[iter] != "R":
            iter += 1
        curr = iter + 1
    print(curr)
