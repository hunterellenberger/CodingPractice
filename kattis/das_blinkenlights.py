from math import lcm

if __name__ == "__main__":
    p, q, s = map(int, input().split())
    if lcm(p, q) > s:
        print("no")
    else:
        print("yes")
