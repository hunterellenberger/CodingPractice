if __name__ == "__main__":
    words = input().split()

    best = ["", 0]
    for i in range(0, len(words)):
        count = 0
        for j in range(i, len(words)):
            if words[i] == words[j]:
                count += 1
            if best[1] < count:
                best[0] = words[i]
                best[1] = count
            if words[i] != words[j]:
                break

    print(best[0])
