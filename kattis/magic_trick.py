if __name__ == "__main__":
    cards = input()
    cards2 = set(cards)
    if len(cards) > len(cards2):
        print("0")
    else:
        print("1")
