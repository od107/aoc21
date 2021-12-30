from day15.chiton import *


def test_part1():
    assert lowest_risk("day15/data/simple_test_data") == 9
    assert lowest_risk("day15/data/test_data") == 40
    assert lowest_risk("day15/data/real_data") == 441


# def test_part2():
#     assert fast_polymer("day14/data/test_data", 1) == 1
#     assert fast_polymer("day14/data/test_data", 10) == 1588
#     assert fast_polymer("day14/data/real_data", 10) == 2947
#     assert fast_polymer("day14/data/test_data", 40) == 2188189693529
#     assert fast_polymer("day14/data/real_data", 40) == 3232426226464