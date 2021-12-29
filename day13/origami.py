def origami(file, folds=None):
    data, instructions = readfile(file)

    # new_data = data
    for i, instr in enumerate(instructions):
        if folds is not None and i >= folds:
            break
        if instr[0] == "y":
            y = instr[1]
            for point in data:
                if point[1] > y:
                    point[1] = 2 * y - point[1]
        else:
            x = instr[1]
            for point in data:
                if point[0] > x:
                    point[0] = 2 * x - point[0]
        data = set(tuple(sub) for sub in data)
        data = [list(sub) for sub in data]

    pretty_print(data)

    return len(data)


def pretty_print(data):
    max_x, max_y = 0, 0
    for el in data:
        if el[0] > max_x:
            max_x = el[0]
        if el[1] > max_y:
            max_y = el[1]
    data.sort()
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if [x, y] in data:
                print("x", end='')
            else:
                print(" ", end='')
        print()


def readfile(file):
    data = []
    instructions = []
    end_data = False
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line == "\n":
                end_data = True
                continue
            if not end_data:
                point = line.strip().split(",")
                point = [int(coord) for coord in point]
                data += [point]
            else:
                instruction = [line[11:12], int(line[13:].strip())]
                instructions += [instruction]
    return data, instructions


def main():
    print("the answer is ")
    print(origami("data/test_data", 1))
    print(origami("data/real_data", 1))
    print(origami("data/test_data"))
    print(origami("data/real_data"))


if __name__ == "__main__":
    main()
