def bingo(file):
    with open(file) as f:
        drawn = f.readline().strip().split(",")

        #todo: create board object to hold 5x5 times an int + a boolean
        
        for next_line in f:
            value = list(next_line.strip())



def main():
    print("the answer is ")
    print(bingo("data/test_data"))
    print(bingo("data/real_data"))
#    print(life_support("data/test_data"))
#    print(life_support("data/real_data"))


if __name__ == "__main__":
    main()
