from day4.bingo import *

def test_bingo():
    assert bingo("day4/data/test_data") == 4512
    assert bingo("day4/data/real_data") == 28082

#def test_life_support():
#    assert life_support("day3/data/test_data") == 230
#    assert life_support("day3/data/real_data") == 2990784