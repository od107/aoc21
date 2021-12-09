from day2.calc_coordinates import *

def test_calc_coordinates():
    assert calc_coordinates("day2/data/testdata") == 150
    assert calc_coordinates("day2/data/real_data") == 2215080
