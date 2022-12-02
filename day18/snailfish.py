def add(file):
    values = readfile(file)

    result = values[0]

    for line in values[1:]:
        result = insert(result, line)
        exploded, splitted = True, True
        while exploded or splitted:
            result, exploded = explode(result)
            if exploded:
                continue
            result, splitted = split(result)

    return result


def insert(a, b):
    return "[" + a + "," + b + "]"


def split(expr):
    splitted = False

    for i, letter in enumerate(expr[1:], start=1):
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
            # splitted = True
            leftidx = i
            ldigits = 1
            rdigits = 1
            while char(expr[i]):
                i += 1

            while expr[i+ldigits] != ',':
                ldigits += 1
            left_value = ''
            for j in range(ldigits):
                left_value += expr[i+j]
            i += 1 + ldigits

            while expr[i+rdigits] != ']':
                rdigits += 1
            right_value = ''
            for j in range(rdigits):
                right_value += expr[i+j]
            right_idx = i + rdigits

            break

    if exploded:
        right_string = expr[right_idx + 1:]
        left_string = expr[:leftidx]
        r_digits = 1
        l_digits = 1
        for i, letter in enumerate(expr[right_idx:]):
            if not char(letter):
                while not char(expr[right_idx+i+r_digits]):
                    letter += expr[right_idx+i+r_digits]
                    r_digits += 1

                right_string = expr[right_idx+1:i+right_idx] \
                                + str(int(letter) + int(right_value)) \
                                + expr[right_idx+i+r_digits:]
                break

        for i, letter in reversed(list(enumerate(expr[:leftidx]))):
            if not char(letter):
                while not char(expr[i-l_digits]):
                    letter += expr[i-l_digits]
                    l_digits += 1
                letter = letter[::-1]

                left_string = expr[:i-l_digits+1]
                left_string += str(int(letter) + int(left_value))
                left_string += expr[i+1:leftidx]
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
    # split('[[[[0,7],4],[15,[0,13]]],[1,1]]')
    # print(explode('[7,[6,[5,[4,[3,2]]]]]'))
    print(add("data/test_data6"))
    # print(add("data/test_data4"))
    # print(explode('[[[[[15,123]],[3,87]]]]'))
    # print(explode('[[3,[2,[10,[7,3]]]],[60,[5,[4,[3,2]]]]]'))


if __name__ == "__main__":
    main()
