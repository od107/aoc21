from collections import Counter, deque, defaultdict
import sys, heapq, datetime


def lowest_risk(file, big=False):
    data = get_data(file)

    if big:
        width = len(data[0])
        height = len(data)
        new_map = [[0 for x in range(width * 5)] for y in range(height * 5)]
        for i in range(5):
            for j in range(5):
                for x in range(width):
                    for y in range(height):
                        value = (data[y][x] + i + j)
                        if value > 9:
                            value -= 9
                        new_map[height * j + y][width * i + x] = value
        data = new_map

    dest = (len(data[0])-1, len(data)-1)

    pqueue = []
    considered_list = []
    entry_finder = defaultdict(def_value)
    for y, row in enumerate(data):
        for x, risk in enumerate(row):
            new_node = Node(x, y, risk)
            pqueue.append(new_node)
            entry_finder[(x, y)] = new_node
    end_node = find(pqueue, dest[0], dest[1])
    heapq.heapify(pqueue)

    while pqueue:
        current_node = heapq.heappop(pqueue)
        del entry_finder[(current_node.x, current_node.y)]
        if current_node.removed:
            continue
        considered_list += [current_node]
        if current_node == end_node:
            break
        neighbors = []
        for x in range(max(0, current_node.x-1), min(dest[1]+1, current_node.x+2)):
            if x == current_node.x:
                continue
            neighbor = entry_finder[(x, current_node.y)]
            if neighbor:
                neighbors += [neighbor]

        for y in range(max(0, current_node.y-1), min(dest[1]+1, current_node.y+2)):
            if y == current_node.y:
                continue
            neighbor = entry_finder[(current_node.x, y)]
            if neighbor:
                neighbors += [neighbor]

        for neighbor in neighbors:
            alt = current_node.dist + neighbor.risk
            if alt < neighbor.dist:
                # found this performance gain with removed status in the heapq documentation
                neighbor.removed = True
                new_node = Node(neighbor.x, neighbor.y, neighbor.risk)
                new_node.dist = alt
                new_node.parent = current_node
                heapq.heappush(pqueue, new_node)
                entry_finder[(new_node.x, new_node.y)] = new_node

    current_node = find(considered_list, dest[0], dest[1])
    return current_node.dist


def def_value():
    return None


def find(arr, x, y):
    for el in arr:
        if not el.removed and el.x == x and el.y == y:
            return el


class Node:
    def __init__(self, x, y, risk):
        self.x = x
        self.y = y
        self.dist = sys.maxsize
        self.parent = None
        self.risk = risk
        if x == 0 and y == 0:
            self.dist = 0
            self.risk = 0
        self.removed = False

    def __lt__(self, other):
        return self.dist < other.dist

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def get_data(file):
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
    # print(lowest_risk("data/simple_test_data", True))
    # print(lowest_risk("data/test_data", True))
    start_time = datetime.datetime.now()
    print(lowest_risk("data/real_data", True))
    end_time = datetime.datetime.now()
    print(end_time - start_time)


if __name__ == "__main__":
    main()
