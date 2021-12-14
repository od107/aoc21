def lose_bingo(file):
    drawn, boards = load_data(file)
    losing_board, losing_number = draw_numbers_lose(drawn, boards)
    return calc_score(losing_board, losing_number)


def win_bingo(file):
    drawn, boards = load_data(file)
    winning_board, winning_number = draw_numbers_win(drawn, boards)
    return calc_score(winning_board, winning_number)


def load_data(file):
    boards = []
    with open(file) as f:
        drawn = f.readline().strip().split(",")

        while True:
            values = [''] * 5
            line = f.readline()
            if not line:
                break
            for i in range(5):
                values[i] = f.readline().strip().split()
            boards.append(Board(values))
    return drawn, boards


def draw_numbers_lose(drawn, boards):
    won_boards = set()
    for number in drawn:
        for board in boards:
            board.mark_number(number)
            if board.won:
                won_boards.add(board)
                if len(won_boards) == len(boards):
                    return board, number


def draw_numbers_win(drawn, boards):
    for number in drawn:
        for board in boards:
            board.mark_number(number)
            if board.won:
                return board, number


def calc_score(board, number):
    sum = 0
    for i in range(5):
        for j in range(5):
            if not board.drawn[i][j]:
                sum += int(board.values[i][j])
    return sum * int(number)


class Board:
    def __init__(self, values):
        self.values = values
        self.drawn = [[False for i in range(5)] for j in range(5)]
        self.won = False

    def mark_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.values[i][j] == number:
                    self.drawn[i][j] = True
                    self.check_if_won(i, j)

    def check_if_won(self, i, j):
        for x in range(5):
            if not self.drawn[x][j]:
                break
            if x == 4:
                self.won = True
        for y in range(5):
            if not self.drawn[i][y]:
                break
            if y == 4:
                self.won = True


def main():
    print("the answer is ")
    print(win_bingo("data/test_data"))
    print(win_bingo("data/real_data"))
    print(lose_bingo("data/test_data"))
    print(lose_bingo("data/real_data"))


if __name__ == "__main__":
    main()
