def count_more(file):
    return count_avg(file,1)

def count_avg(file, window):
    f = open(file, "r")
    values = [0] * window
    last_sum = 0
    for i in range(window):
        values[i] = int(f.readline().strip())
        last_sum += values[i]
    count = 0
    for next in f:
        next = int(next.strip())
        new_sum = last_sum - values[0] + next
        if new_sum > last_sum:
            count += 1
        for i in range(1,window):
            values[i-1] = values[i]
        values[window-1] = next
        last_sum = new_sum
    return count


def main():
    print("the answer is ")
    print(count_more("data/real_data"))
    print(count_avg("data/real_data",3))

if __name__ == "__main__":
    main()

