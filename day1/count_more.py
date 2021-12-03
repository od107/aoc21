def count_more(file):
    f = open(file, "r")
    last = int(f.readline().strip())
    count = 0
    for next in f:
        next = int(next.strip())
        if next > last:
            count += 1
        last = next
    return count

def count_avg(file):
    f = open(file, "r")
    two_before_last = int(f.readline().strip())
    before_last = int(f.readline().strip())
    last = int(f.readline().strip())
    last_sum = two_before_last + before_last + last
    count = 0
    for next in f:
        next = int(next.strip())
        new_sum = next + last + before_last
        if new_sum > last_sum:
            count += 1
        before_last = last
        last = next
        last_sum = new_sum
    return count


def main():
    print("the answer is ")
    print(count_more("../data/real_data_day1"))
    print(count_avg("../data/real_data_day1"))

if __name__ == "__main__":
    main()

