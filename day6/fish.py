def fish(file, days):
    fishes = readfile(file)

    for day in range(days):
        new_fishes = []
        for i, fish in enumerate(fishes):
            fishes[i] -= 1
            if fishes[i] == -1:
                fishes[i] = 6
                new_fishes.append(8)
        fishes += new_fishes

    return len(fishes)


def fish_fast(file, days):
    fishes = readfile(file)
    fish_buckets = [0] * 9
    # lets store the fishes in a list of 8 with each bucket the number of fish and the days before reproducing
    for fish in fishes:
        fish_buckets[fish] += 1

    for day in range(days):
        new_buckets = [0] * 9
        for i, number_of_fish in reversed(list(enumerate(fish_buckets))):
            if i == 0:
                new_buckets[6] += number_of_fish
                new_buckets[8] = number_of_fish
            else:
                new_buckets[i-1] = fish_buckets[i]
        fish_buckets = new_buckets

    sum = 0
    for fishes in fish_buckets:
        sum += fishes
    return sum


def readfile(file):
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            fishes = text_line.strip().split(",")
            fishes = [int(fish) for fish in fishes]
    return fishes


def main():
    print("the answer is ")
    print(fish("data/test_data", 18))
    print(fish("data/test_data", 80))
    print(fish("data/real_data", 80))
    print(fish_fast("data/test_data", 256))
    print(fish_fast("data/real_data", 256))


if __name__ == "__main__":
    main()
