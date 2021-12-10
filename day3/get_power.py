

def get_power(file):
    f = open(file, "r")
    value = list(f.readline().strip())
    global result
    result = [0] * len(value)
    handle_input_bits(value)
    for next in f:
        value = list(next.strip())
        handle_input_bits(value)
    gamma, epsilon = calculate_epsilon_gamma()
    f.close()
    return gamma * epsilon


def calculate_epsilon_gamma():
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


if __name__ == "__main__":
    main()
