import sys

def seven_digit(file):
    file_input = readfile(file)

    count = 0
    for number in file_input:
        if len(number) == 2 or len(number) == 3 or len(number) == 4 or len(number) == 7:
            count += 1

    return count


def readfile(file):
    results = []
    with open(file) as f:
        while True:
            text_line = f.readline()
            if not text_line:
                break
            file_input = text_line.strip().split(" | ")
            results += file_input[1].split(" ")
    return results


def main():
    print("the answer is ")
    print(seven_digit("data/test_data"))
    print(seven_digit("data/real_data"))
#    print(position_crabs("data/test_data", True))
#    print(position_crabs("data/real_data", True))


if __name__ == "__main__":
    main()
