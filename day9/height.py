def height(file):
    height_map = readfile(file)
    lowest_values = []
    low_points = []

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
            low_points += [[x, y]]

    basin_sizes = []
    for point in low_points:
        basin_sizes += [find_basin_size(point, height_map)]
    basin_sizes.sort(reverse=True)
    basin_result = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    return sum(lowest_values), basin_result


def find_basin_size(start_point, height_map):
    basin_coordinates = [start_point]
    to_process = basin_coordinates.copy()
    map_max_x = len(height_map[0]) - 1
    map_max_y = len(height_map) - 1

    while to_process:
        point = to_process.pop()
        if point[0] != 0:
            check_coordinate([point[0]-1, point[1]], basin_coordinates, to_process, height_map)
        if point[0] < map_max_x:
            check_coordinate([point[0]+1, point[1]], basin_coordinates, to_process, height_map)
        if point[1] != 0:
            check_coordinate([point[0], point[1]-1], basin_coordinates, to_process, height_map)
        if point[1] < map_max_y:
            check_coordinate([point[0], point[1]+1], basin_coordinates, to_process, height_map)

    return len(basin_coordinates)


def check_coordinate(point, basin_coordinates, to_process, height_map):
    if point not in basin_coordinates and height_map[point[1]][point[0]] != 9:
        to_process += [point]
        basin_coordinates += [point]


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
