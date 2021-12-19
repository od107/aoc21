def fish(file, days):
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            fishes = text_line.strip().split(",")
            fishes = [int(fish) for fish in fishes]

    for day in range(days):
        new_fishes = []
        for i, fish in enumerate(fishes):
            fishes[i] -= 1
            if fishes[i] == -1:
                fishes[i] = 6
                new_fishes.append(8)
        fishes += new_fishes

    return len(fishes)


def main():
    print("the answer is ")
    print(fish("data/test_data", 18))
    print(fish("data/test_data", 80))
    print(fish("data/real_data", 80))
#    print(vents("data/test_data", False))
#    print(vents("data/real_data", False))


if __name__ == "__main__":
    main()
