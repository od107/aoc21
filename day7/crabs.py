import sys


def position_crabs(file, incr=False):
    crabs = readfile(file)

    lower = min(crabs)
    upper = max(crabs)
    lowest_score = sys.maxsize

    if incr:
        incr_cost = calc_incr_cost(upper-lower)

    for pos in range(lower, upper):
        if not incr:
            fuel = calc_fuel(pos, crabs)
        else:
            fuel = calc_fuel_incr(pos, crabs, incr_cost)
        if fuel < lowest_score:
            lowest_score = fuel

    return lowest_score


def calc_incr_cost(spread):
    incr_cost = [0] * (spread + 1)
    cost = 1
    for i in range(1, spread + 1):
        incr_cost[i] = incr_cost[i-1] + cost
        cost += 1
    return incr_cost


def calc_fuel(pos, crabs):
    fuel = 0
    for crab in crabs:
        fuel += abs(pos-crab)
    return fuel


def calc_fuel_incr(pos, crabs, incr_cost):
    fuel = 0
    for crab in crabs:
        idx = abs(pos - crab)
        fuel += incr_cost[idx]
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
    print(position_crabs("data/test_data"))
    print(position_crabs("data/real_data"))
    print(position_crabs("data/test_data", True))
    print(position_crabs("data/real_data", True))


if __name__ == "__main__":
    main()
