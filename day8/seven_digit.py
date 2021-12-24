def seven_digit(file):
    file_input = readfile(file)
    count = 0
    for line in file_input:
        for number in line[1]:
            if len(number) == 2 or len(number) == 3 or len(number) == 4 or len(number) == 7:
                count += 1
    return count


def total_output(file):
    file_input = readfile(file)
    total = 0
    for [training, result] in file_input:
        dict_display = determine_numbers(training)
        value = determine_value(dict_display, result)
        total += value
    return total


def determine_value(dict_display, result):
    value = 0
    for number in result:
        value *= 10
        value += dict_display[number]
    return value


def determine_numbers(training):
    number_dict = {}
    number_list = [''] * 10
    six_segment_nr = []
    five_segment_nr = []
    for number in training:
        if len(number) == 2:
            number_list[1] = number
        elif len(number) == 3:
            number_list[7] = number
        elif len(number) == 4:
            number_list[4] = number
        elif len(number) == 7:
            number_list[8] = number
        elif len(number) == 6:
            six_segment_nr += [number]
        elif len(number) == 5:
            five_segment_nr += [number]

    segment_a = number_list[7].replace(number_list[1][0], '').replace(number_list[1][1], '')
    for number in six_segment_nr:
        for char in number_list[7]:
            if char not in number:
                number_list[6] = number
                six_segment_nr.remove(number)
                break
    for number in six_segment_nr:
        for char in number_list[4]:
            if char not in number:
                number_list[0] = number
                six_segment_nr.remove(number)
                break
    number_list[9] = six_segment_nr[0]

    segment_c = [char for char in number_list[1] if char not in number_list[6]][0]
    for number in five_segment_nr:
        if segment_c not in number:
            number_list[5] = number
            five_segment_nr.remove(number)
            break
    segment_f = [char for char in number_list[1] if char in number_list[5]][0]
    for number in five_segment_nr:
        if segment_f in number:
            number_list[3] = number
        else:
            number_list[2] = number

    for i, v in enumerate(number_list):
        number_dict[v] = i

    return number_dict


def readfile(file):
    file_input = []
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            line = text_line.strip().split(" | ")
            line[0] = line[0].split(" ")
            line[0] = ["".join(sorted(value)) for value in line[0]]
            line[1] = line[1].split(" ")
            line[1] = ["".join(sorted(value)) for value in line[1]]
            file_input += [line]
    return file_input


def main():
    print("the answer is ")
    print(seven_digit("data/test_data"))
    print(seven_digit("data/real_data"))
    print(total_output("data/test_data"))
    print(total_output("data/real_data"))


if __name__ == "__main__":
    main()
