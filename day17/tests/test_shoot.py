from day17.shoot import *


def test_part1():
    assert angle("day17/data/test_data", True) == 45
    assert angle("day17/data/real_data", True) == 3655


def test_part2():
    assert angle("day17/data/test_data") == 112
    assert angle("day17/data/real_data") == 1447

