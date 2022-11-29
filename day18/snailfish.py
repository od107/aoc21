def add(file):
    values = readfile(file)

    result = values[0]

    for line in values[1:]:
        result = insert(result, line)
        exploded = True
        while (exploded):
            result, exploded = explode(result)


    return result


def insert(a, b):
    return "[" + a + "," + b + "]"


def split(value):
    return value


def explode(expr):
    depth = 0
    exploded = False

    for i, letter in enumerate(expr):
        if letter == "[":
            depth += 1
        elif letter == "]":
            depth -= 1
        if depth == 5:
            exploded = True
            leftidx = i
            while char(expr[i]):
                i += 1
            # todo add support for numbers with 2 chars
            left_value = expr[i]
            leftvalidx = i
            i += 2
            right_value = expr[i]
            rightidx = i+1
            break

    if exploded:
        right_string = expr[rightidx + 1:]
        left_string = expr[:leftidx]
        for i, letter in enumerate(expr[rightidx:]):
            if not char(letter):
                # todo add support for numbers with 2 chars
                right_string = expr[rightidx+1:i+rightidx] \
                                + str(int(letter) + int(right_value)) \
                                + expr[rightidx+i+1:]
                break

        for i, letter in reversed(list(enumerate(expr[:leftidx]))):
            if not char(letter):
                left_string = expr[:i]  \
                    + str(int(letter) + int(left_value)) \
                    + expr[i+1:leftidx]
                break

        expr = left_string + '0' + right_string

    return expr, exploded


def char(ch):
    if ch == "[" or ch == "]" or ch == ",":
        return True
    return False


def magnitude(value):
    return value


def readfile(file):
    file_input = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            file_input += [line]
    return file_input


def main():
    print("the answer is ")
    print(explode('[7,[6,[5,[4,[3,2]]]]]'))
    # print(add("data/test_data4"))


if __name__ == "__main__":
    main()
