def calc_coordinates(file):
    x = 0
    y = 0
    f = open(file, "r")
    for next in f:
        command = next.strip().split()
        value = int(command[1])
        if command[0] == "forward":
            x += value
        elif command[0] == "down":
            y += value
        elif command[0] == "up":
            y -= value
    f.close()
    return x * y

def new_calc_coordinates(file):
    x = 0
    y = 0
    aim = 0
    f = open(file, "r")
    for next in f:
        command = next.strip().split()
        value = int(command[1])
        if command[0] == "forward":
            x += value
            y += aim * value
        elif command[0] == "down":
            aim += value
        elif command[0] == "up":
            aim -= value
    return x * y

def main():
    print("the answer is ")
    print(calc_coordinates("data/testdata"))
    print(calc_coordinates("data/real_data"))
    print(new_calc_coordinates("data/testdata"))
    print(new_calc_coordinates("data/real_data"))

if __name__ == "__main__":
    main()
