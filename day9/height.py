def height(file):
    height_map = readfile(file)
    lowest_values = []

    for y, line in enumerate(height_map):
        for x, value in enumerate(line):
            if x != 0 and height_map[y][x-1] <= value:
                continue
            if x < len(line)-1 and height_map[y][x+1] <= value:
                continue
            if y != 0 and height_map[y-1][x] <= value:
                continue
            if y < len(height_map)-1 and height_map[y+1][x] <= value:
                continue
            lowest_values += [value + 1]

    return sum(lowest_values)


def readfile(file):
    file_input = []
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            line = text_line.strip()
            line = [int(x) for x in line]
            file_input += [line]
    return file_input


def main():
    print("the answer is ")
    print(height("data/test_data"))
    print(height("data/real_data"))
#    print(total_output("data/test_data"))
#    print(total_output("data/real_data"))


if __name__ == "__main__":
    main()
