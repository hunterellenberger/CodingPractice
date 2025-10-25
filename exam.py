if __name__ == "__main__":
    correct = int(input())
    you = input()
    friend = input()

    same = 0
    different = 0
    for i in range(len(you)):
        if you[i] == friend[i]:
            same = same + 1
        else:
            different = different + 1

    if same < correct:
        print(same + (different - (correct - same)))
    elif same > correct:
        print(correct + different)
    else:
        print(len(you))
