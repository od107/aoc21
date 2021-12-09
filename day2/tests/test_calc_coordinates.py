from day2.calc_coordinates import *

def test_calc_coordinates():
    assert calc_coordinates("day2/data/testdata") == 150
    assert calc_coordinates("day2/data/real_data") == 2215080

def test_new_calc_coordinates():
    assert new_calc_coordinates("day2/data/testdata") == 900
    assert new_calc_coordinates("day2/data/real_data") == 1864715580
