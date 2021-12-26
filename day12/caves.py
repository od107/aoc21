

def calc_paths(file):
    data = readfile(file)

    
    return number_of_paths


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
    # print(calc_paths("data/less_simple_cave"))
    # print(calc_paths("data/larger_cave"))
    # print(calc_paths("data/real_data"))


if __name__ == "__main__":
    main()
