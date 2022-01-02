from day16.decoder import *


def test_part1():
    assert decode("day16/data/test_data") == 16
    assert decode("day16/data/test_data_2") == 12
    assert decode("day16/data/test_data_3") == 23
    assert decode("day16/data/test_data_4") == 31
    assert decode("day16/data/real_data") == 979

#
# def test_part2():
#     assert lowest_risk("day15/data/test_data", True) == 315
#     assert lowest_risk("day15/data/real_data", True) == 2849
