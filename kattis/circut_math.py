if __name__ == "__main__":
    symbols = ["*", "+", "-"]
    inputs = int(input())
    variables = input().split()
    circut = input().split()

    mapping = dict()


    for i in range(len(circut)):
        if circut[i] not in symbols:
            if circut[i] in mapping:
                circut[i] = mapping[circut[i]]
            else:
                mapping[circut[i]] = variables[0]
                circut[i] = variables.pop(0)

    iter = 0
    while len(circut) > 1:
        if circut[iter] == "*" and (circut[iter - 1] == "F" or circut[iter - 2] == "F"):
            circut[iter] = "F"
            circut.pop(iter-1)
            iter -= 1
            circut.pop(iter-1)
            iter -= 1
        elif circut[iter] == "*" and (circut[iter - 1] == "T" and circut[iter - 2] == "T"):
            circut[iter] = "T"
            circut.pop(iter-1)
            iter -= 1
            circut.pop(iter-1)
            iter -= 1
        elif circut[iter] == "+" and (circut[iter - 1] == "F" and circut[iter - 2] == "F"):
            circut[iter] = "F"
            circut.pop(iter-1)
            iter -= 1
            circut.pop(iter-1)
            iter -= 1
        elif circut[iter] == "+" and (circut[iter - 1] == "T" or circut[iter - 2] == "T"):
            circut[iter] = "T"
            circut.pop(iter-1)
            iter -= 1
            circut.pop(iter-1)
            iter -= 1
        elif circut[iter] == "-":
            if circut[iter - 1] == "F":
                circut[iter] = "T"
                circut.pop(iter-1)
                iter -= 1
            else:
                circut[iter] = "F"
                circut.pop(iter-1)
                iter -= 1
        iter += 1
    print(circut[0])
