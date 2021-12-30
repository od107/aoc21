from day14.polymer import *


def test_part1():
    assert slow_polymer("day14/data/test_data", 10) == 1588
    assert slow_polymer("day14/data/real_data", 10) == 2947


def test_part2():
    assert fast_polymer("day14/data/test_data", 1) == 1
    assert fast_polymer("day14/data/test_data", 10) == 1588
    assert fast_polymer("day14/data/real_data", 10) == 2947
    assert fast_polymer("day14/data/test_data", 40) == 2188189693529
    assert fast_polymer("day14/data/real_data", 40) == 3232426226464