if __name__ == "__main__":
    answers = []
    time = 0
    correct = 0

    answer = input()
    while answer != "-1":
        answers.append(answer)
        answer = input()
    for answer in range(len(answers)):
        answers[answer] = answers[answer].split()

    for answer in answers:
        if answer[2] == "right":
            time += int(answer[0])
            correct += 1
        else:
            time += 20

    for i in answers:
        neverRight = 0
        for j in range(answers.index(i), len(answers)):
            if i[1] == answers[j][1] and (i[2] == "right" or answers[j][2] == "right"):
                neverRight = 1
        if neverRight == 0:
            time -= 20

    print(correct, time)
