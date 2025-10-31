from random import randint

if __name__ == "__main__":
    choices = ['A', 'B', 'C']
    i = 0
    changeUp = 0

    while i < 1000:
        picked = []
        choice = choices[randint(0, 2)]
        picked.append(choice)
        print(choice)

        marilyn = input().split()
        picked.append(marilyn[0])
        if int(marilyn[1]) == 1:
            choice = marilyn[0]
            print(choice)
        else:
            choice = list(set(choices) - set(picked))[0]
            print(choice)
            changeUp += randint(0, 3)

        input()
        i += 1
