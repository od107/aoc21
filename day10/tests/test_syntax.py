from day10.syntax import *


def test_part1():
    assert syntax("day10/data/test_data")[0] == 26397
    assert syntax("day10/data/real_data")[0] == 411471


def test_part2():
    assert syntax("day10/data/test_data")[1] == 288957
    assert syntax("day10/data/real_data")[1] == 3122628974
