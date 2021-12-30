from collections import Counter, deque
import operator


def lowest_risk(file):
    global data
    data = readfile(file)
    global dest
    dest = (len(data[0])-1, len(data)-1)

    #implement A*
    start = Node(0, 0)
    to_process = [start]
    nodes_considered = []

    while to_process:
        # current implementation delivers all points considered. Need to have backtracking
        current_node = to_process.pop()
        nodes_considered += [current_node]
        if current_node.x == dest[0] and current_node.y == dest[1]:
            break
        for x in range(max(0, current_node.x-1), min(dest[1], current_node.x+2)):
            if x == current_node.x:
                continue
            new_node = Node(x, current_node.y, current_node)
            if new_node not in nodes_considered and new_node not in to_process:
                to_process += [new_node]

        for y in range(max(0, current_node.y-1), min(dest[1], current_node.y+2)):
            if y == current_node.y:
                continue
            new_node = Node(current_node.x, y, current_node)
            if new_node not in nodes_considered and new_node not in to_process:
                to_process += [new_node]
        to_process.sort(key=operator.attrgetter('g'))

    # construct path via backtracking
    current_node = nodes_considered[-1]
    path = []
    while current_node.parent is not None:
        path.append(current_node)
        current_node = current_node.parent

    total_risk = 0
    for node in path:
        total_risk += node.f
    return total_risk


class Node:
    global data
    global dest

    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        if parent is None:
            self.f = 0
        else:
            self.f = parent.f + data[y][x]
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
