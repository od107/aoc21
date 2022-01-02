from collections import Counter, deque, defaultdict
import sys, heapq, datetime


def decode(file):
    data = get_data(file)
    binary = bin(int(data, 16))[2:].zfill(4 * len(data))

    idx = 0
    versions = 0
    idx, versions = parse(binary, idx, versions)

    return versions


def parse(binary, idx, versions):
    versions += int(binary[idx:idx + 3], 2)
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
    else: #operator
        length_type_ID = binary[idx]
        idx += 1
        if length_type_ID == "0":
            nr_of_bits = int(binary[idx:idx+15], 2)
            idx += 15
            end_pos = idx + nr_of_bits
            while idx < end_pos:
                idx, versions = parse(binary, idx, versions)
        else:
            nr_of_packets = int(binary[idx:idx + 11], 2)
            idx += 11
            for i in range(nr_of_packets):
                idx, versions = parse(binary, idx, versions)
    return idx, versions


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
    print(decode("data/test_data"))
    print(decode("data/real_data"))
    # print(decode("data/test_data"))

    # start_time = datetime.datetime.now()

    # end_time = datetime.datetime.now()
    # print(end_time - start_time)


if __name__ == "__main__":
    main()
