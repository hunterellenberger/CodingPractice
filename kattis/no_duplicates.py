if __name__ == "__main__":
    words = input().split(" ")
    seen = []
    fail = 0

    for word in words:
        if word in seen:
            fail = 1
        else:
            seen.append(word)

    if fail == 0:
        print("yes")
    else:
        print("no")
