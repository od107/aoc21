from day7.crabs import *


def test_part1():
    assert position_crabs("day7/data/test_data") == 37
    assert position_crabs("day7/data/real_data") == 356179


def test_part2():
    assert position_crabs("day7/data/test_data", True) == 168
    assert position_crabs("day7/data/real_data", True) == 99788435