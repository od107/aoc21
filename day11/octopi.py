flashes = 0
octopi = {}

def calc_flashes(file):
    global octopi
    global flashes
    data = readfile(file)
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            octopi[str(x) + "," + str(y)] = Octopus(x, y, int(value))
    for step in range(100):
        for octopus in octopi.values():
            octopus.increase()
        for octopus in octopi.values():
            octopus.reset_flash()
    return flashes


class Octopus:

    def __init__(self, x_pos, y_pos, energy):
        self.x_pos = x_pos
        self.y_pos = y_pos
 #       self.coordinates = coordinates
        self.energy = energy
        self.flashed = False

 #       self.drawn = [[False for i in range(5)] for j in range(5)]

    def increase(self):
        if not self.flashed:
            self.energy += 1
            if self.energy > 9:
                self.flash()

    def flash(self):
        global flashes
        self.flashed = True
        self.energy = 0
        flashes += 1
        id_list = self._find_neighbours()
        for ident in id_list:
            octopi[ident].increase()

    def _find_neighbours(self):
        id_list= []
        x_list = [self.x_pos]
        y_list = [self.y_pos]
        if self.x_pos > 0:
            x_list.append(self.x_pos - 1)
        if self.x_pos < 9:
            x_list.append(self.x_pos + 1)
        if self.y_pos > 0:
            y_list.append(self.y_pos - 1)
        if self.y_pos < 9:
            y_list.append(self.y_pos + 1)
        for x in x_list:
            for y in y_list:
                id_list.append(str(x) + "," + str(y))
        return id_list

    def reset_flash(self):
        self.flashed = False


def readfile(file):
    file_input = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            line = [x for x in line]
            file_input += [line]
    return file_input


def main():
    print("the answer is ")
    print(calc_flashes("data/test_data"))
    print(calc_flashes("data/real_data"))


if __name__ == "__main__":
    main()
