def polymer(file, steps):
    template, inserts = readfile(file)

    for step in range(steps):
        to_insert= []
        for insert in inserts:
            for index, _ in enumerate(template):
                if template.startswith(insert[0], index):
                    to_insert += [[index+1, insert[1]]]
        template = insert_in_template(template, to_insert)

    counts = {}
    for char in template:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] = counts[char] + 1

    minimum = min(counts.values())
    maximum = max(counts.values())

    return maximum - minimum


def insert_in_template(template, to_insert):
    to_insert.sort(reverse=True)
    for index, char in to_insert:
        template = template[:index] + char + template[index:]
    return template


def readfile(file):
    inserts = []

    with open(file) as f:
        template = f.readline().strip()
        f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            insert = line.strip().split(" -> ")
            inserts += [insert]
    return template, inserts


def main():
    print("the answer is ")
    print(polymer("data/test_data", 10))
    print(polymer("data/real_data", 10))
    # print(polymer("data/test_data", 40))
    # print(polymer("data/real_data"; 40))


if __name__ == "__main__":
    main()
