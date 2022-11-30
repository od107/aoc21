def add(file):
    values = readfile(file)

    result = values[0]

    for line in values[1:]:
        result = insert(result, line)
        exploded, splitted = True, True
        while exploded or splitted:
            result, exploded = explode(result)
            result, splitted = split(result)

    return result


def insert(a, b):
    return "[" + a + "," + b + "]"


def split(expr):
    splitted = False

    for i, letter in enumerate(expr[1:], start=1):
        # if i == 0:
        #     continue
        if not char(letter) and not char(expr[i-1]):
            val = 10 * int(expr[i-1]) + int(letter)
            leftval = val // 2
            rightval = (val+1) // 2
            right_string = expr[i + 1:]
            left_string = expr[:i-1]
            expr = left_string + '[' + str(leftval) + ',' + str(rightval) + ']' + right_string
            splitted = True
            break

    return expr, splitted


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
    split('[[[[0,7],4],[15,[0,13]]],[1,1]]')
    # print(explode('[7,[6,[5,[4,[3,2]]]]]'))
    # print(add("data/test_data4"))


if __name__ == "__main__":
    main()
