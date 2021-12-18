#
def vents(file, only_straight=True):
    ground_map = [[0 for i in range(1000)] for j in range(1000)]
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            points = text_line.strip().split(" -> ")

            line = [point.split(",") for point in points]
            line = [[int(coord) for coord in point if coord != ''] for point in line]

            if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
                add_straight_path(line, ground_map)
            elif not only_straight:
                add_diag_path(line, ground_map)

    score = calc_score(ground_map)
    return score


def add_diag_path(line, ground_map):
    if line[0][0] > line[1][0]:
        line = [line[1], line[0]]
    if line[0][1] < line[1][1]:
        up = True
    else:
        up = False

    start_x = line[0][0]
    start_y = line[0][1]

    if up:
        for i in range(line[1][0] - line[0][0] + 1):
            ground_map[start_x + i][start_y + i] += 1
    else:
        for i in range(line[1][0] - line[0][0] + 1):
            ground_map[start_x + i][start_y - i] += 1


def add_straight_path(line, ground_map):
    min_x = min(line[0][0], line[1][0])
    max_x = max(line[0][0], line[1][0])
    min_y = min(line[0][1], line[1][1])
    max_y = max(line[0][1], line[1][1])

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            ground_map[x][y] += 1


def calc_score(ground_map):
    sum = 0
    for i in range(1000):
        for j in range(1000):
            if ground_map[i][j] > 1:
                sum += 1
    return sum


def main():
    print("the answer is ")
    print(vents("data/test_data"))
    print(vents("data/real_data"))
    print(vents("data/test_data", False))
    print(vents("data/real_data", False))


if __name__ == "__main__":
    main()
