from day15.chiton import *


def test_part1():
    assert lowest_risk("day15/data/simple_test_data") == 9
    assert lowest_risk("day15/data/test_data") == 40
    assert lowest_risk("day15/data/real_data") == 441


def test_part2():
    assert lowest_risk("day15/data/test_data", True) == 315
    assert lowest_risk("day15/data/real_data", True) == 2849