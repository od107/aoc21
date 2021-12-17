#
def vents(file):
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
                add_path(line, ground_map)
    score = calc_score(ground_map)
    return score


def add_path(line, ground_map):
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
    # print(lose_bingo("data/test_data"))
    # print(lose_bingo("data/real_data"))


if __name__ == "__main__":
    main()
