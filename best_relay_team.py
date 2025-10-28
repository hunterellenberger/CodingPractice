if __name__ == "__main__":
    people = int(input())
    racers = []
    for _ in range(people):
        racer = input().split()
        racers.append(racer)

    print(racers)
