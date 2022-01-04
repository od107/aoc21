import math
from collections import Counter, deque, defaultdict
import sys, heapq, datetime


def decode(file, hex=None):
    if file:
        data = get_data(file)
    else:
        data = hex
    binary = bin(int(data, 16))[2:].zfill(4 * len(data))

    idx, versions, value = parse(binary, 0)

    return versions, value


def parse(binary, idx):
    version = int(binary[idx:idx + 3], 2)
    deeper_version = 0
    type_ID = int(binary[idx+3:idx+6], 2)
    idx += 6
    if type_ID == 4: #literal
        bin_value = binary[idx+1:idx+5]
        char = binary[idx:idx+5]
        idx += 5
        while char[0] == "1":
            bin_value += binary[idx+1:idx+5]
            char = binary[idx:idx+5]
            idx += 5
        value = int(bin_value, 2)

    else:  # operator
        values = []
        length_type_ID = binary[idx]
        idx += 1
        if length_type_ID == "0":
            nr_of_bits = int(binary[idx:idx+15], 2)
            idx += 15
            end_pos = idx + nr_of_bits
            while idx < end_pos:
                idx, deeper_version, value = parse(binary, idx)
                version += deeper_version
                values.append(value)
        else:
            nr_of_packets = int(binary[idx:idx + 11], 2)
            idx += 11
            for i in range(nr_of_packets):
                idx, deeper_version, value = parse(binary, idx)
                version += deeper_version
                values.append(value)
        if type_ID == 0:
            value = sum(values)
        elif type_ID == 1:
            value = math.prod(values)
        elif type_ID == 2:
            value = min(values)
        elif type_ID == 3:
            value = max(values)
        elif type_ID == 5:
            value = values[0] > values[1]
        elif type_ID == 6:
            value = values[0] < values[1]
        elif type_ID == 7:
            value = values[0] == values[1]

    return idx, version, value


def get_data(file):
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            data = line.strip()
    return data


def main():
    print("the answer is ")
    # print(decode("data/simplest_test"))
    # print(decode("data/test_data_2"))
    print(decode("data/real_data"))
    # print(decode("data/test_data"))


if __name__ == "__main__":
    main()
