import sys


def crabs(file):
    crabs = readfile(file)

    lower = min(crabs)
    upper = max(crabs)
    lowest_score = sys.maxsize

    for pos in range(lower, upper):
        fuel = calc_fuel(pos, crabs)
        if fuel < lowest_score:
            lowest_score = fuel

    return lowest_score


def calc_fuel(pos, crabs):
    fuel = 0
    for crab in crabs:
        fuel += abs(pos-crab)
    return fuel


def readfile(file):
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            crabs = text_line.strip().split(",")
            crabs = [int(crab) for crab in crabs]
    return crabs


def main():
    print("the answer is ")
    print(crabs("data/test_data"))
    print(crabs("data/real_data"))
#    print(fish_fast("data/test_data", 256))
#    print(fish_fast("data/real_data", 256))


if __name__ == "__main__":
    main()
