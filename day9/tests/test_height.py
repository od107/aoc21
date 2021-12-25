from day9.height import *


def test_part1():
    assert height("day9/data/test_data")[0] == 15
    assert height("day9/data/real_data")[0] == 550


def test_part2():
    assert height("day9/data/test_data")[1] == 1134
    assert height("day9/data/real_data")[1] == 1100682