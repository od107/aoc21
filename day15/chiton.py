from collections import Counter, deque


def lowest_risk(file):
    data = readfile(file)
    dest = (len(data[0])-1, len(data)-1)

    #implement A*
    start = Node(0, 0, dest)
    to_process = [start]
    path = []

    while to_process:
        current_node = to_process.pop()
        path += [current_node]
        if current_node.x == dest[0] and current_node.y == dest[1]:
            break
        for x in range(max(0, current_node.x-1), min(dest[1], current_node.x+2)):
            if x == current_node.x:
                continue
            new_node = Node(x, current_node.y, dest, current_node)
            if new_node not in path:
                to_process += [new_node]

        for y in range(max(0, current_node.y-1), min(dest[1], current_node.y+2)):
            if y == current_node.y:
                continue
            new_node = Node(current_node.x, y, dest, current_node)
            if new_node not in path:
                to_process += [new_node]
        to_process.sort()

    total_risk = 0
    for node in path:
        total_risk += node.f
    return total_risk


class Node:
    def __init__(self, x, y, dest, parent=None):
        self.x = x
        self.y = y
        if parent is None:
            self.f = 0
        else:
            self.f = parent.f
        self.h = abs(dest[0]-x) + abs(dest[1]-y)
        self.g = self.f + self.h

    def __lt__(self, other):
        return self.g < other.g

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def readfile(file):
    data = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            risk = [int(char) for char in line]
            data += [risk]
    return data


def main():
    print("the answer is ")
    print(lowest_risk("data/test_data"))
    # print(lowest_risk("data/real_data"))


if __name__ == "__main__":
    main()
