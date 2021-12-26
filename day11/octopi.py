flashes = 0
octopi = {}


def calc_flashes(file, steps=100):
    global octopi
    global flashes
    flashes = 0
    flashes_at_100 = 0
    step_all_flash = 0
    data = readfile(file)
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            octopi[str(x) + "," + str(y)] = Octopus(x, y, int(value))

    all_flash = False
    while not all_flash:
        all_flash = True
        for octopus in octopi.values():
            octopus.increase()
        for octopus in octopi.values():
            if not octopus.flashed:
                all_flash = False
            octopus.reset_flash()
        step_all_flash += 1
        print_octo(step_all_flash)
        if step_all_flash == 100:
            flashes_at_100 = flashes
    return flashes_at_100, step_all_flash


def print_octo(step):
    print("step: " + str(step))
    for y in range(10):
        for x in range(10):
            print(octopi[str(x)+ "," + str(y)].energy, end=" ")
        print(" ")
    print(" ")


class Octopus:

    def __init__(self, x_pos, y_pos, energy):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.energy = energy
        self.flashed = False

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
