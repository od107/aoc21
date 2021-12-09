def calc_coordinates(file):
    x = 0
    y = 0
    f = open(file, "r")
    for next in f:
        command = next.strip().split()
        if command[0] == "forward":
            x += int(command[1])
        elif command[0] == "down":
            y += int(command[1])
        elif command[0] == "up":
            y -= int(command[1])
    return x * y


def main():
    print("the answer is ")
    print(calc_coordinates("data/testdata"))
    print(calc_coordinates("data/real_data"))

if __name__ == "__main__":
    main()
