

def calc_paths(file):
    caves = {}
    data = readfile(file)

    for line in data:
        for item in line:
            if item not in caves:
                caves[item] = Cave(item)
        if line[1] not in caves[line[0]].links:
            caves[line[0]].add_link(line[1])
            caves[line[1]].add_link(line[0])

    paths = []
    explore(caves, caves["start"], paths)

    return len(paths)


def explore(caves, cave, paths, path=None):
    if not path:
        path = []

    path.append(cave.name)
    if cave.name == "end":
        print(path)
        paths += [path.copy()]
        return

    for link in cave.links:
        if link.isupper() or link not in path:
            explore(caves, caves[link], paths, path.copy())


class Cave:
    def __init__(self, name):
        self.name = name
        self.links = []

    def add_link(self, link):
        self.links.append(link)


def readfile(file):
    file_input = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().split("-")
            file_input += [line]
    return file_input


def main():
    print("the answer is ")
    print(calc_paths("data/simple_cave"))
    print(calc_paths("data/less_simple_cave"))
    print(calc_paths("data/larger_cave"))
    print(calc_paths("data/real_data"))


if __name__ == "__main__":
    main()
