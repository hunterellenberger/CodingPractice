if __name__ == "__main__":
    key, test = input().split()
    fail = 0
    key = list(key)
    for letter in range(len(test)):
        if test[letter] in key and test[letter] == key[0]:
            key.pop(0)
        elif test[letter] in key and test[letter] != key[0]:
            fail = 1

    if fail == 1 or key:
        print("FAIL")
    else:
        print("PASS")
