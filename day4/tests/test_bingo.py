from day4.bingo import *

def test_bingo_win():
    assert win_bingo("day4/data/test_data") == 4512
    assert win_bingo("day4/data/real_data") == 28082

def test_bingo_lose():
    assert lose_bingo("day4/data/test_data") == 1924
    assert lose_bingo("day4/data/real_data") == 8224