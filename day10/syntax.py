def syntax(file):
    parentheses_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    data = readfile(file)
    score = 0
    for line in data:
        count_round = 0
        count_square = 0
        count_curly = 0
        count_tag = 0
        last_chars = []
        for char in line:
            if char == "(":
                count_round += 1
                last_chars += char
            elif char == "[":
                count_square += 1
                last_chars += char
            elif char == "{":
                count_curly += 1
                last_chars += char
            elif char == "<":
                count_tag +=1
                last_chars += char
            elif char == ")":
                if last_chars[-1] == "(":
                    count_round -= 1
                    del last_chars[-1]
                else:
                    score += 3
                    break
            elif char == "]":
                if last_chars[-1] == "[":
                    count_square -= 1
                    del last_chars[-1]
                else:
                    score += 57
                    break
            elif char == "}":
                if last_chars[-1] == "{":
                    count_curly -= 1
                    del last_chars[-1]
                else:
                    score += 1197
                    break
            elif char == ">":
                if last_chars[-1] == "<":
                    count_tag -= 1
                    del last_chars[-1]
                else:
                    score += 25137
                    break
    return score


def readfile(file):
    file_input = []
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            line = text_line.strip()
            line = [x for x in line]
            file_input += [line]
    return file_input

def main():
    print("the answer is ")
    print(syntax("data/test_data"))
    print(syntax("data/real_data"))
#    print(total_output("data/test_data"))
#    print(total_output("data/real_data"))


if __name__ == "__main__":
    main()
