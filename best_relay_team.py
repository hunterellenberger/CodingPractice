if __name__ == "__main__":
    people = int(input())
    racers = list()
    finalTeam = []
    first = []
    other = []

    for _ in range(people):
        racer = input().split()
        racers.append(racer)
        first.append(float(racer[1]))
        other.append(float(racer[2]))

    firstTotal = sum(first)
    otherTotal = sum(other)
    first.sort()
    other.sort()

    for _ in range(4):
        if first[0] / firstTotal > other[0] / otherTotal:
            for racer in racers:
                print(racer)
                if first[0] == float(racer[1]):
                    finalTeam.append(racer)
                    break
            first.pop(0)
        else:
            for racer in racers:
                if other[0] == float(racer[2]):
                    finalTeam.append(racer[0])
                    break
            other.pop(0)
