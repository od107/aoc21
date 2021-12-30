from collections import Counter


def slow_polymer(file, steps):
    template, inserts = readfile(file)

    for step in range(steps):
        to_insert = []
        for insert in inserts:
            for index, _ in enumerate(template):
                if template.startswith(insert, index):
                    to_insert += [[index+1, inserts[insert]]]
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


def fast_polymer(file, steps):
    template, inserts = readfile(file)

    # don't construct the string. Just keep track of the count of each 2-letter grouping
    letterpair_template_count = Counter()
    for i in range(1, len(template)):
        letters = template[i-1]+template[i]
        letterpair_template_count[letters] += 1

    for step in range(steps):
        # AB->C becomes AC, CB
        transform_count = Counter()
        for elem in letterpair_template_count:
            if elem in inserts:
                transform_count[elem[0] + inserts[elem]] += letterpair_template_count[elem]
                transform_count[inserts[elem] + elem[1]] += letterpair_template_count[elem]
        letterpair_template_count = transform_count

    # count result
    char_count = Counter()
    for elem in letterpair_template_count:
        char_count[elem[0]] += letterpair_template_count[elem]
    char_count[template[-1]] += 1
    return max(char_count.values())-min(char_count.values())


def insert_in_template(template, to_insert):
    to_insert.sort(reverse=True)
    for index, char in to_insert:
        template = template[:index] + char + template[index:]
    return template


def readfile(file):
    inserts = {}

    with open(file) as f:
        template = f.readline().strip()
        f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            insert = line.strip().split(" -> ")
            inserts[insert[0]] = insert[1]
    return template, inserts


def main():
    print("the answer is ")
    # print(slow_polymer("data/test_data", 10))
    # print(slow_polymer("data/real_data", 10))
    print(fast_polymer("data/test_data", 40))
    # print(fast_polymer("data/test_data", 40))
    print(fast_polymer("data/real_data", 40))


if __name__ == "__main__":
    main()
