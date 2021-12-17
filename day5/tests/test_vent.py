from day5.vents import *


def test_vents():
    assert vents("day5/data/test_data") == 5
    assert vents("day5/data/real_data") == 7438

# def test_bingo_lose():
#     assert lose_bingo("day5/data/test_data") == 1924
#     assert lose_bingo("day5/data/real_data") == 8224