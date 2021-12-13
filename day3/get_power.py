def life_support(file):
    f = open(file, "r")
    o_list, co2_list = [], []
    for next_line in f:
        value = list(next_line.strip())
        o_list.append(value)
    co2_list = o_list.copy()

    clean_list(o_list, False)
    clean_list(co2_list, True)

    oxygen = to_decimal(o_list)
    co2 = to_decimal(co2_list)

    return oxygen * co2


def to_decimal(single_record):
    decimal = 0
    base = 1
    for bit in reversed(single_record[0]):
        if bit == "1":
            decimal += 1 * base
        base *= 2
    return decimal


def clean_list(input_list, is_co2):
    to_remove = []
    for bit_index in range(len(input_list[0])):
        if len(input_list) == 1:
            break
        mcv = most_common_value(input_list, bit_index, is_co2)
        for item in input_list:
            if (item[bit_index] != mcv and is_co2 == False) \
                    or (item[bit_index] == mcv and is_co2 == True):
                to_remove.append(item)
        for item in to_remove:
            input_list.remove(item)
        to_remove.clear()


def most_common_value(input_list, bit_index, is_co2):
    count_ones, count_zeros = 0, 0
    for item in input_list:
        if item[bit_index] == "1":
            count_ones += 1
        else:
            count_zeros += 1
    if count_ones > count_zeros:
        value = "1"
    elif count_ones < count_zeros:
        value = "0"
    else:
        value = "1"
    return value


def get_power(file):
    f = open(file, "r")
    value = list(f.readline().strip())
    global result
    result = [0] * len(value)
    handle_input_bits(value)
    for next_line in f:
        value = list(next_line.strip())
        handle_input_bits(value)
    f.close()
    gamma, epsilon = calc_epsilon_gamma()
    return gamma * epsilon


def calc_epsilon_gamma():
    gamma = 0
    epsilon = 0
    base = 1
    for bit in reversed(result):
        if bit > 0:
            gamma += 1 * base
        else:
            epsilon += 1 * base
        base *= 2
    return gamma, epsilon


def handle_input_bits(value):
    for i in range(len(value)):
        if value[i] == "0":
            result[i] -= 1
        else:
            result[i] += 1


def main():
    print("the answer is ")
    print(get_power("data/test_data"))
    print(get_power("data/real_data"))
    print(life_support("data/test_data"))
    print(life_support("data/real_data"))

if __name__ == "__main__":
    main()
