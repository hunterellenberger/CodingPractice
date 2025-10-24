if __name__ == "__main__":
    total = int(input())
    names = []
    seenNames = []
    ascending = 0
    descending = 0
    neither = 0

    for i in range(total):
        names.append(input())

    for name in range(total - 1):
        if names[name] in seenNames:
            neither = 1
        seenNames.append(names[name])
        if ascending == 0 and names[name] <= names[name + 1]:
            ascending = 1
        elif descending == 0 and names[name] >= names[name + 1]:
            descending = 1
        if ascending == 1 and names[name] >= names[name + 1]:
            neither = 1
        if descending == 1 and names[name] <= names[name + 1]:
            neither = 1

    if neither == 1:
        print("NEITHER")
    elif descending == 1:
        print("DECREASING")
    else:
        print("INCREASING")
