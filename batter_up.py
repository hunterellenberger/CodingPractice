if __name__ == "__main__":
    time = int(input())
    bats = list(map(int, input().split()))
    length = len(bats) - 1
    bats2 = [i for i in bats if i != -1]
    time = len(bats2)

    print(sum(bats2) / time)
