def bingo(file):
    with open(file) as f:
        drawn = f.readline().strip().split(",")

        values = [''] * 5
        boards = []

        while True:
            line = f.readline()
            if not line:
                break
            for i in range(5):
                values[i] = f.readline().strip().split()
            boards.append(Board(values))

    winning_board, winning_number = draw_numbers(drawn, boards)
    return calc_score(winning_board, winning_number)


def calc_score(board, number):
    sum = 0
    for i in range(5):
        for j in range(5):
            if not board.drawn[i][j]:
                sum += int(board.values[i][j])
    return sum * int(number)


def draw_numbers(drawn, boards):
    for number in drawn:
        for board in boards:
            board.mark_number(number)
            if board.won:
                return board, number


class Board:
    values = [''] * 5
    drawn = [[False] * 5] * 5
    won = False

    def __init__(self, values):
        self.values = values

    def mark_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.values[i][j] == number:
                    self.drawn[i][j] = True
                    self.check_if_won(i, j)

    def check_if_won(self, i, j):
        for x in range (5):
            if not self.drawn[x][j]:
                break
            if x == 4:
                self.won = True
        for y in range (5):
            if not self.drawn[i][y]:
                break
            if x == 4:
                self.won = True

def main():
    print("the answer is ")
    print(bingo("data/test_data"))
#    print(bingo("data/real_data"))
#    print(life_support("data/test_data"))
#    print(life_support("data/real_data"))


if __name__ == "__main__":
    main()
