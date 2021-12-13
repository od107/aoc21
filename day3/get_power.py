def life_support(file):
    f = open(file, "r")
    input_list = []
    for next in f:
        value = list(next.strip())
        input_list.append(value)
    oxygen, co2 = calc_oxygen_co2(input_list)
    return oxygen * co2


def calc_oxygen_co2(input_list):
    o_list = input_list.copy()
    co2_list = input_list.copy()

    clean_list(o_list, False)
    clean_list(co2_list, True)

    oxygen = to_decimal(o_list)
    co2 = to_decimal(co2_list)

    return oxygen, co2


def to_decimal(single_record):
    decimal = 0
    base = 1
    for bit in reversed(single_record[0]):
        if bit == "1":
            decimal += 1 * base
        base *= 2
    return decimal


def clean_list(input_list, is_co2):
    for bit_index in range(len(input_list[0])):
        mcv = most_common_value(input_list, bit_index)
        if mcv != "equal":
            for item in input_list:
                if (item[bit_index] != mcv and is_co2 == True) \
                        or (item[bit_index] == mcv and is_co2 == False):
                    input_list.remove(item)
                if len(input_list) == 1:
                    break


def most_common_value(input_list, bit_index):
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
        value = "equal"
    return value


def get_power(file):
    f = open(file, "r")
    value = list(f.readline().strip())
    global result
    result = [0] * len(value)
    handle_input_bits(value)
    for next in f:
        value = list(next.strip())
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
    # print(get_power("data/test_data"))
    # print(get_power("data/real_data"))
    print(life_support("data/test_data"))
    print(life_support("data/real_data"))

if __name__ == "__main__":
    main()
