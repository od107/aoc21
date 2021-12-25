def syntax(file):
    autocomplete_score = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    data = readfile(file)
    score_corrupt = 0
    score_incomplete = []
    for i, line in enumerate(data):
        last_chars = []
        for char in line:
            if char == "(":
                last_chars += char
            elif char == "[":
                last_chars += char
            elif char == "{":
                last_chars += char
            elif char == "<":
                last_chars += char
            elif char == ")":
                if last_chars[-1] == "(":
                    del last_chars[-1]
                else:
                    score_corrupt += 3
                    break
            elif char == "]":
                if last_chars[-1] == "[":
                    del last_chars[-1]
                else:
                    score_corrupt += 57
                    break
            elif char == "}":
                if last_chars[-1] == "{":
                    del last_chars[-1]
                else:
                    score_corrupt += 1197
                    break
            elif char == ">":
                if last_chars[-1] == "<":
                    del last_chars[-1]
                else:
                    score_corrupt += 25137
                    break
            elif char == "\n":
                temp_score = 0
                for item in reversed(last_chars):
                    temp_score *= 5
                    temp_score += autocomplete_score[item]
                score_incomplete += [temp_score]

    if len(score_incomplete) % 2 == 0:
        raise Exception("length incomplete score is even")
    score_incomplete.sort()
    middle_idx = len(score_incomplete)//2
    return score_corrupt, score_incomplete[middle_idx]


def readfile(file):
    file_input = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = [x for x in line]
            file_input += [line]
    return file_input


def main():
    print("the answer is ")
    print(syntax("data/test_data"))
    print(syntax("data/real_data"))


if __name__ == "__main__":
    main()
